#!/usr/bin/env python
"""
This script merges all given PDF files from the parameters into one big PDF file.
"""

import sys
from PyPDF2 import PdfFileMerger
from PyPDF2.utils import PdfReadError

FILENAME = "result.pdf"


def read_args():
    """
    Returns values from args in a list.
    """
    arglist = sys.argv[1:]
    if arglist != []:
        return arglist
    else:
        print("Missing PDF file names in parameter.")
        exit()


def merge_pdfs():
    """
    Main loop
    """
    pdfs = read_args()
    merger = PdfFileMerger()

    try:
        for pdf in pdfs:
            merger.append(open(pdf, 'rb'))
        with open(FILENAME, 'wb') as fout:
            merger.write(fout)
    except PdfReadError as not_pdf:
        print(not_pdf)
        print("Are you sure all of these are PDF files?!")
        exit()
    except FileNotFoundError as no_file:
        print(no_file)
        print("Try entering existing files")
        exit()
    print("Successfully merged PDF files into '"+FILENAME+"'")


if __name__ == "__main__":
    merge_pdfs()
