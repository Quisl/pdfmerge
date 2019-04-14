#!/usr/bin/env python
"""
This script merges all given PDF files from the parameters into one big PDF file.
"""

import sys
from PyPDF2 import PdfFileMerger
from PyPDF2.utils import PdfReadError

FILENAME = "result.pdf"

def readArgs():
    """
    Returns values from args in a list.
    """
    arglist = sys.argv[1:]
    if arglist != []:
        return arglist
    else:
        print("Missing PDF file names in parameter.")
        exit()

def mergePDFs():
    """
    Main loop
    """
    pdfs = readArgs()
    merger = PdfFileMerger()

    try:
        for pdf in pdfs:
            merger.append(open(pdf, 'rb'))
        with open(FILENAME, 'wb') as fout:
            merger.write(fout)
    except PdfReadError as notPdf:
        print (notPdf)
        print ("Are you sure all of these are PDF files?!")
        exit()
    except FileNotFoundError as noFile:
        print (noFile)
        print ("Try entering existing files")
        exit()
    print("Successfully merged PDF files into '"+FILENAME+"'")

if __name__ == "__main__":
    mergePDFs()
