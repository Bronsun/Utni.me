from flask import render_template, url_for, flash, redirect,request,Blueprint,send_file,send_from_directory
import os
import PyPDF4
import datetime
import time
import random


PDF=Blueprint('PDF',__name__)


@PDF.route('/main_pdf')
def main_pdf():
   return render_template('main_pdf.html')

@PDF.route('/pdf')
def show():
   return render_template('pdf.html')


@PDF.route('/pdf_merge',methods=['GET','POST'])
def pdf():
   pdfWriter = PyPDF4.PdfFileWriter()
   if request.method == 'POST':
      files_to_upload = request.files.getlist("pdf")
      print(len(files_to_upload))
      for item in files_to_upload:
         f = item
         f.save(f.filename)
         pdfFileObj = open(f.filename, 'rb')
         pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
         for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
  
   file_name_pdf = '../utnime.pdf'
   pdfOutput=open(file_name_pdf,'wb')
   x=pdfWriter.write(pdfOutput)
   time.sleep(5)
   pdfOutput.close()
   print('KURWA')
   
   '''
   for item in files_to_upload:
      f=item
      
      os.remove(f.filename)
   '''
   return send_file(file_name_pdf,as_attachment=True)




   '''
         pdfFileObj = open(f.filename,'rb')
         pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
         for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            
         file_name_pdf = 'utnime.pdf'
         pdfOutput = open(file_name_pdf,'wb')
         pdfWriter.write(pdfOutput)
         pdfOutput.close()
         
         return send_file(file_name_pdf,as_attachment=True)
   '''
   
   
   
   
   
   '''
   error=None
   if request.method == "POST":
      if request.files:
         pdf = request.files["pdf"]
         if pdf.filename=="":
            error=("Brak nazwy pliku :(")
         pdf.save(os.path.join("neuro/PDF/InputFiles",pdf.filename))
         print("IMAGE SAVED")
         return redirect(request.url)
   '''
   
    
    