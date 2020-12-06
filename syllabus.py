"""
syllabus parser file
author: rad 
.txt files only

don't ruin this file rosie please
"""
import datetime as dt
import json
import io

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams


#f = open("CS 250 Syllabus.txt", "r")
f = open('pdf_test.pdf', 'rb')

def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    #codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()
    return data

def parsetxt(file):
    out = {}
    for line in file:
        if "-" in str(line):
            linelist = line.split(" - ")
            work = linelist[0]
            date = linelist[1][:len(linelist[1]) - 1]
            datetemp = dt.datetime.strptime(date, "%m/%d/%Y")
            datestr = datetemp.strftime("%m/%d/%Y")
            out.update({work:datestr})
    return out

def parsepdf(file):
    out = {}
    for line in file.split("\n"):
        if "-" in line:
            linelist = line.split(" - ")
            work = linelist[0]
            date = linelist[1][:len(linelist[1]) - 1]
            datetemp = dt.datetime.strptime(date, "%m/%d/%Y")
            datestr = datetemp.strftime("%Y-%m-%d")
            out.update({work:datestr})
    return out



if __name__ == "__main__":
    #print(parsetxt(f))
    print(parsepdf(pdfparser('pdf_test.pdf')))

