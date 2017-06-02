pdfbooktool
===========

A python 3 tool for use in creating your own books.

The input PDF can be of any size, and the default output is an A4 PDF,
ready to print twosided, cut, and bind to A6 books using the "perfect
binding" method. Optionally, one can print on A5 paper, fold, and bind
to an A6 book, using the same method.

This package installs a script called 'booktool' and this is what you would 
actually use for preparing your PDFs.


Usage
-----

In a terminal, navigate to the directory of your PDF, then do:

```
$ booktool input-file.pdf
```

Or optionally:

```
$ booktool --a5paper input-file.pdf
```

For A5-sized paper output.

This will output a couple of intermediary files (which will be removed once the
script is finished running) into the working directory, and eventually a file
called "out.pdf". This new file is a reordered PDF, ready for double-sided 
printing. Use "long edge binding" as your double-sided setting on 
your printer for A4. If you opted for A5 paper, use "short edge" instead.

Once printed, you can cut the sheets in half (only needed if you print in A4) 
and bind them together using a technique called "perfect binding". There exist
several videos on youtube that explains how to do this.

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
