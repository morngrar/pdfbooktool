pdfbooktool
===========

A python 3 tool for use in creating your own books.

There is currently only support for handling books in A6 format, printing on
A4 paper. However, the input PDF can be any size.

This package installs a script called 'booktool' and this is what you would
actually use for preparing your PDFs.


Usage
-----

Navigate to the directory of your PDF, then do:

$ booktool input-file.pdf

This will output a couple of intermediary files (which will be removed once the
script is finished running) into the working directory, and eventually a file
called 'out.pdf'. This new file is a reordered PDF in A4 dimensions, ready for
double-sided printing. Once printed, you can cut the sheets in half and bind
them together.

The easiest way is to fold the cut sheets and using the 'perfect binding'
technique. There exist several videos on youtube that explains how to do this.

A good open-source tool for creating suitable PDFs is 'scribus'.


Requirements
------------

This package requires 'PyPDF2' to work, the install process should install this
automatically if needed.


Running under windows
---------------------

Running this script under Windows has not been tested, but neither PyPDF2 nor
pdfbooktool uses any features that are platform specific.
