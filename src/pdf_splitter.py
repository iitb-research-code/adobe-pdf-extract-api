from PyPDF2 import PdfWriter, PdfReader
import math
import sys
import os


def split_pdf(pdf_path):
    pdfnames=[]
    max_page_per_pdf = 100      # Increase this if adobe relaxes maximum number of pages per request
    inputpdf = PdfReader(open(pdf_path, "rb"))
    no_pages = len(inputpdf.pages)
    # no_pages = 50
    #no_pdfs = math.ceil(no_pages/max_page_per_pdf)      # Stores the number of PDFs after splitting
    #pages_per_pdf = math.ceil(no_pages/no_pdfs)
    pdf_no = 1
    split_pdf = PdfWriter()
    for i in range(1,no_pages + 1):
        split_pdf.add_page(inputpdf.pages[i-1])
        if i % max_page_per_pdf == 0 or i == no_pages:
            new_pdf_name = pdf_path[:pdf_path.rindex('.')] + "_" + str(pdf_no) + ".pdf"
            new_pdf_name = new_pdf_name.replace(' ', '')
            pdfnames.append(new_pdf_name)
            with open(new_pdf_name, "wb") as outputStream:         # Writes a PDF when:
                split_pdf.write(outputStream)                      # the number of pages covered in original PDF is multiple of pages_per_pdf  
            split_pdf = PdfWriter()                            # or if we have reached end of original PDF
            pdf_no += 1
    #os.remove(pdf_path)
    return pdfnames

files = split_pdf(sys.argv[1])
print(files)



# Run Adobe Script
