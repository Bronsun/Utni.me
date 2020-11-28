from PyPDF4 import PdfFileReader, PdfFileWriter
import os
def merge_pdfs(paths,output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output,'wb') as out:
        pdf_writer.write(out)

if __name__=='__main__':
    paths = ['../../dummy.pdf','../../sample.pdf']
    merge_pdfs(paths,output='../../merged.pdf')
