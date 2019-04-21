polyglot
========

<img src="http://i.imgur.com/eifuDPP.png" alt="image" width="300" />

*A python package and command-line tools for translating documents and
webpages to various markup languages and document formats (html, epub,
mobi ..)*.

[![Documentation Status](https://readthedocs.org/projects/pypolyglot/badge/)](http://pypolyglot.readthedocs.io/en/latest/?badge)

[![Coverage Status](https://cdn.rawgit.com/thespacedoctor/polyglot/master/coverage.svg)](https://cdn.rawgit.com/thespacedoctor/polyglot/master/htmlcov/index.html)

Here's a summary of what's included in the python package:

Command-Line Usage
==================

    Documentation for polyglot can be found here: http://pypolyglot.readthedocs.org/en/stable

    Translate documents and webpages to various markup languages and document formats (html, epub, mobi ..)

    Usage:
        polyglot init
        polyglot [-oc] (pdf|html|epub|mobi) <url> [<destinationFolder> -f <filename> -s <pathToSettingsFile>]
        polyglot kindle <url> [-f <filename> -s <pathToSettingsFile>]
        polyglot [-o] (epub|mobi) <docx> [<destinationFolder> -f <filename> -s <pathToSettingsFile>]
        polyglot kindle <docx> [-f <filename> -s <pathToSettingsFile>]
        polyglot [-o] kindleNB2MD <notebook> [<destinationFolder> -s <pathToSettingsFile>]

    Options:
        init                                                            setup the polyglot settings file for the first time
        pdf                                                             print webpage to pdf
        html                                                            parse and download webpage to a local HTML document
        epub                                                            generate an epub format book from a webpage URL
        kindle                                                          send webpage article straight to kindle

        -h, --help                                                      show this help message
        -v, --version                                                   show version
        -o, --open                                                      open the document after creation
        -c, --clean                                                     add polyglot's clean styling to the output document
        <url>                                                           the url of the article's webpage
        <docx>                                                          path to a DOCX file
        -s <pathToSettingsFile>, --settings <pathToSettingsFile>        path to alternative settings file (optional)
        <destinationFolder>                                             the folder to save the parsed PDF or HTML document to (optional)
        -f <filename>, --filename <filename>                            the name of the file to save, otherwise use webpage title as filename (optional)

Documentation
=============

Documentation for polyglot is hosted by [Read the
Docs](http://pypolyglot.readthedocs.org/en/stable/) (last [stable
version](http://pypolyglot.readthedocs.org/en/stable/) and [latest
version](http://pypolyglot.readthedocs.org/en/latest/)).

Installation
============

The easiest way to install polyglot is to use `pip`:

    pip install polyglot

Or you can clone the [github
repo](https://github.com/thespacedoctor/polyglot) and install from a
local version of the code:

    git clone git@github.com:thespacedoctor/polyglot.git
    cd polyglot
    python setup.py install

To upgrade to the latest version of polyglot use the command:

    pip install polyglot --upgrade

Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

    git clone git@github.com:thespacedoctor/polyglot.git
    cd polyglot
    python setup.py develop

[Pull requests](https://github.com/thespacedoctor/polyglot/pulls) are
welcomed!

### Sublime Snippets

If you use [Sublime Text](https://www.sublimetext.com/) as your code
editor, and you're planning to develop your own python code with
polyglot, you might find [my Sublime
Snippets](https://github.com/thespacedoctor/polyglot-Sublime-Snippets)
useful.

Issues
------

Please report any issues
[here](https://github.com/thespacedoctor/polyglot/issues).

License
=======

Copyright (c) 2018 David Young

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
