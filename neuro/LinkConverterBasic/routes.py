from flask import render_template, url_for, flash, redirect,request,Blueprint
from neuro import app,db,bcrypt
from neuro.modules import User,UserLink

LinkConvBasic = Blueprint('LinkConvBasic',__name__)

@LinkConvBasic.route('/<short_url>')
def redirect_to_url(short_url):
    link = UserLink.query.filter_by(short_url=short_url).first_or_404()
    return redirect(link.original_url) 


@LinkConvBasic.route('/add_link', methods=['POST'])
def add_link():
    error=None
    link=UserLink.query.count()+1000
    users=User.query.count()+2000
    original_url = request.form['original_url']
    if original_url=="":
        error="Z pustego linku nic nie wyczarujemy :("
        return render_template('main.html',error=error,users=users,link=link)
    else:    
        link = UserLink(original_url=original_url)
        db.session.add(link)
        db.session.commit()

    return render_template('link_added.html',new_link=link.short_url,original_url=link.original_url,error=error)