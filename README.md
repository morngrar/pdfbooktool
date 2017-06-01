pdfbooktool
===========

A python 3 tool for use in creating your own books.

There is currently only support for handling books in A6 format, printing on
A4 paper. However, the input PDF can be any size.

This package installs a script called 'booktool' and this is what you would
actually use for preparing your PDFs.


Usage
-----

In a terminal, navigate to the directory of your PDF, then do:

```
$ booktool input-file.pdf
```

This will output a couple of intermediary files (which will be removed once the
script is finished running) into the working directory, and eventually a file
called 'out.pdf'. This new file is a reordered PDF with A4 dimensions, ready for
double-sided printing. Once printed, you can cut the sheets in half and bind
them together using a technique called "perfect binding". There exist several 
videos on youtube that explains how to do this.

A good open-source tool for creating suitable PDFs is 'scribus'.


Requirements
------------

This package requires python 3, and the library 'PyPDF2' to work, the install 
process should install this automatically if needed.


Installation
------------

The most convenient way to install pdfbooktool is with pip. Since the script 
currently doesn't seem to work on Windows, installation instructions are only 
given for linux:

Make sure you have python 3 installed, then open a terminal and type:

```
$ sudo pip3 install pdfbooktool
```

This should automatically install the tool, and it's dependencies.


Running under windows
---------------------

Running this script under Windows has barely been testet. Neither PyPDF2 nor
pdfbooktool should use any features that are platform specific, however it 
doesn't seem to currently work under Windows 7. Help with further testing and
making it work, is wanted.
