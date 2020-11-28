from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db,bcrypt
from neuro.modules import UserLink,User
from neuro.LinkAdvanceConverter.forms import ShortURLForm
from flask_login import login_user, current_user, logout_user,login_required

LinkAdvanceConverter = Blueprint('LinkAdvanceConverter',__name__)

@LinkAdvanceConverter.route('/<short_url>')
def redirect_to_short_url(short_url):
    link = UserLink.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()
    return redirect(link.original_url)


@LinkAdvanceConverter.route('/add_short_link',methods=['GET','POST'])
@login_required
def add_short_link():
    form = ShortURLForm()
    original_url = form.url.data
    
    if form.validate_on_submit():
        links=form.url.data
        all_links=links.split(",")
        print(all_links)
        link = UserLink(original_url=original_url,author=current_user)
        link.visits = link.visits + 1
        db.session.commit()
        db.session.add(link)
        db.session.commit()
        return render_template('link_added_user.html',new_link=link.short_url,original_url=link.original_url)
    return render_template('7url.html',form=form)

