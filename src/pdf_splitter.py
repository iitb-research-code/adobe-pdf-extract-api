from PyPDF2 import PdfFileWriter, PdfFileReader
import math
import sys
import os


def split_pdf(pdf_path):
    pdfnames=[]
    max_page_per_pdf = 100      # Increase this if adobe relaxes maximum number of pages per request
    inputpdf = PdfFileReader(open(pdf_path, "rb"))
    no_pages = inputpdf.numPages
    # no_pages = 50
    #no_pdfs = math.ceil(no_pages/max_page_per_pdf)      # Stores the number of PDFs after splitting
    #pages_per_pdf = math.ceil(no_pages/no_pdfs)
    pdf_no = 1
    split_pdf = PdfFileWriter()
    for i in range(1,inputpdf.numPages + 1):
        split_pdf.addPage(inputpdf.getPage(i-1))
        if i % max_page_per_pdf == 0 or i == inputpdf.numPages:
            new_pdf_name = pdf_path[:pdf_path.rindex('.')] + "_" + str(pdf_no) + ".pdf"
            pdfnames.append(new_pdf_name)
            with open(new_pdf_name, "wb") as outputStream:         # Writes a PDF when:
                split_pdf.write(outputStream)                      # the number of pages covered in original PDF is multiple of pages_per_pdf  
            split_pdf = PdfFileWriter()                            # or if we have reached end of original PDF
            pdf_no += 1
    #os.remove(pdf_path)
    return pdfnames

files = split_pdf(sys.argv[1])
print(files)