polygot
=======

*Using the readability parser API generate clean HTML and PDF documents
of articles found on the web*.

Usage
=====

    *CL tool for polygot*

    :Author:
        David Young

    :Date Created:
        September 28, 2015

    Usage:
        polygot url <urlToParse> <destinationFolder> [-s <pathToSettingsFile>]

        -h, --help            show this help message
        -v, --version         show version
        -s, --settings        the settings file
        urlToParse            the url of the article to parse and convert to PDF
        destinationFolder     the folder to add the parsed PDF to

Documentation
=============

Documentation for polygot is hosted by [Read the
Docs](http://polygot.readthedocs.org/en/stable/) (last [stable
version](http://polygot.readthedocs.org/en/stable/) and [latest
version](http://polygot.readthedocs.org/en/latest/)).

Installation
============

The easiest way to install polygot us to use `pip`:

    pip install polygot

Or you can clone the [github
repo](https://github.com/thespacedoctor/polygot) and install from a
local version of the code:

    git clone git@github.com:thespacedoctor/polygot.git
    cd polygot
    python setup.py install

To upgrade to the latest version of polygot use the command:

    pip install polygot --upgrade

Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

    git clone git@github.com:thespacedoctor/polygot.git
    cd polygot
    python setup.py develop

[Pull requests](https://github.com/thespacedoctor/polygot/pulls) are
welcomed!

Issues
------

Please report any issues
[here](https://github.com/thespacedoctor/polygot/issues).

License
=======

Copyright (c) 2016 David Young

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
