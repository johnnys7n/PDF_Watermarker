import os
import sys
import PyPDF2


wtrmark = sys.argv[1]
PDF_file = sys.argv[2]

template = PyPDF2.PdfFileReader(open(PDF_file))
watermark = PyPDF2.PdfFileReader(open(wtrmark))
output = PyPDF2.PdfFileWriter()


def pdf_watermarker():
    # function to add watermarks to PDF files

    dir_list = os.listdir(os.getcwd())
    if 'new_merged_file' not in dir_list:
        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)
        else:
            print('file has already been merged!')
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
