import os
import subprocess
from pyPdf import PdfFileWriter, PdfFileReader
import pdfconv

####start_dir = "C:/Users/glamp/repository/pdf/pdf-statements2/"

def split_pdf(start_dir):
    for (dirpath, dirnames, filenames) in os.walk(start_dir):
        for f in filenames:
            bank_statement = dirpath+"/"+f

            print bank_statement
            inputpdf = PdfFileReader(file(bank_statement, "rb"))
            
            for i in xrange(inputpdf.numPages):
                print i
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                outputStream = file(dirpath+"/bank_statement%s.pdf" % i, "wb")            
                output.write(outputStream)
                outputStream.close()
                try:
                    pdfconv.convert_pdf(dirpath+"/bank_statement%s.pdf" % i, 'html')
                except:
                    pass
