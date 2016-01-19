#!/usr/bin/python3

# pdfbooktool.py - functions for preparing PDFs for book printing.
#    
# Copyright (C) 2016  Svein-Kåre Bjørnsen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# TOOLBOX
##################################
from math import ceil

def ceil_iter(iterable):
    """Takes iterable of floats and returns list of ceil'ed ints"""
    return [int(ceil(elem)) for elem in iterable]

##################################

from PyPDF2 import PdfFileWriter, PdfFileReader

# Reordering schemes
SCHEME_A6_PERFECT = 0
SCHEME_A5_PERFECT = 1

# PDF-specific size dimensions
UNIT_SIZE_A4 = (595.28000, 841.89000)
UNIT_SIZE_A6 = (297.64063, 419.53039)

class PageError(Exception):
    pass

def shuffle_pages(num, scheme):
    """ Takes a number (pages) and the reordering scheme to use.
    Returns a list of indexes to use with page reordering. """
    
    book = []
    counter = 0

    if scheme == SCHEME_A6_PERFECT:
        sequence = [3, -1, 5, 1, -3, -3, -1, -1]
    elif scheme == SCHEME_A5_PERFECT:
        sequence = [3, -1, -1, -1]

    for page in range(num):
        book.append(0)
        
    for page in range(num):
        if counter == len(sequence):
            counter = 0
        book[page] = page + sequence[counter]
        counter += 1

    return book

def calc_pages_to_add(pdfreader, scheme):
    """ Takes a PdfFileReader and scheme. Returns number of pages
        to add for the selected scheme. """
    
    if scheme == SCHEME_A6_PERFECT:
        counter = 0
        pages = pdfreader.getNumPages()
        done = False
        while not done:
            if pages % 8 != 0:
                counter += 1
                pages += 1
            else:
                done = True
        return counter
    else:
        return None

    # TODO A5_PERFECT

def add_blank_pages(pdf_file):
    """ Takes filename of pdf and number of blank pages to append.
        Writes to "output.pdf" in same directory."""

    writer = PdfFileWriter()
    pdf = PdfFileReader(open(pdf_file, "rb"))
    
    for page in pdf.pages:
        writer.addPage(page)

    for page in range(calc_pages_to_add(pdf, SCHEME_A6_PERFECT)):
        writer.addBlankPage()

    with open("aux.pdf", "wb") as f:
        writer.write(f)

def reorder_pages(pdfreader, scheme):
    """ Takes PdfFileReader and reordering scheme. Returns 
        PdfFileWriter, ordered according to scheme. """
    
    pageorder = shuffle_pages( pdfreader.getNumPages(),
                               scheme )
    out = PdfFileWriter()

    for page in pageorder:
        out.addPage(pdfreader.pages[page])
    
    return out

def add_blank_page(writer, unit_size):
    page = writer.addBlankPage(unit_size[0], unit_size[1])
    return page
    
def make_page(writer, reader, offset=0):
    tx = UNIT_SIZE_A6[0]
    ty = UNIT_SIZE_A6[1]
    
    page = add_blank_page(writer, UNIT_SIZE_A4)
    
    page.mergeTranslatedPage(reader.pages[0+offset], 0, ty)
    page.mergeTranslatedPage(reader.pages[1+offset], tx, ty)
    page.mergeTranslatedPage(reader.pages[2+offset], tx, 0)
    page.mergeTranslatedPage(reader.pages[3+offset], 0, 0)
    
def a6_to_a4_merge(pdf_file):
    
    pdf = PdfFileReader(open(pdf_file, "rb"))
    
    if ceil_iter(pdf.pages[0].mediaBox.upperRight) != ceil_iter(UNIT_SIZE_A6):
        raise PageError("Trying to merge PDF that is not A6 as A6")
        
    writer = PdfFileWriter()
    
    number_pages = pdf.getNumPages()
    if number_pages % 4 != 0:
        raise PageError("Number of pages in PDF not divisible by 4")
    
    page_offset = 0
    while page_offset < number_pages:
        make_page(writer, pdf, page_offset)
        page_offset += 4
    
    with open("out.pdf", "wb") as f:
        writer.write(f)

