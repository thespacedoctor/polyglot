simpdf 
=========================

*Using the readability parser API generate clean HTML and PDF documents of articles found on the web*.

Usage
======

.. code-block:: bash 
   
    
    *CL tool for simpdf*
    
    :Author:
        David Young
    
    :Date Created:
        September 28, 2015
    
    Usage:
        simpdf url <urlToParse> <destinationFolder> [-s <pathToSettingsFile>]
    
        -h, --help            show this help message
        -v, --version         show version
        -s, --settings        the settings file
        urlToParse            the url of the article to parse and convert to PDF
        destinationFolder     the folder to add the parsed PDF to
    

Documentation
=============

Documentation for simpdf is hosted by `Read the Docs <http://simpdf.readthedocs.org/en/stable/>`__ (last `stable version <http://simpdf.readthedocs.org/en/stable/>`__ and `latest version <http://simpdf.readthedocs.org/en/latest/>`__).

Installation
============

The easiest way to install simpdf us to use ``pip``:

.. code:: bash

    pip install simpdf

Or you can clone the `github repo <https://github.com/thespacedoctor/simpdf>`__ and install from a local version of the code:

.. code:: bash

    git clone git@github.com:thespacedoctor/simpdf.git
    cd simpdf
    python setup.py install

To upgrade to the latest version of simpdf use the command:

.. code:: bash

    pip install simpdf --upgrade


Development
-----------

If you want to tinker with the code, then install in development mode.
This means you can modify the code from your cloned repo:

.. code:: bash

    git clone git@github.com:thespacedoctor/simpdf.git
    cd simpdf
    python setup.py develop

`Pull requests <https://github.com/thespacedoctor/simpdf/pulls>`__
are welcomed!


Issues
------

Please report any issues
`here <https://github.com/thespacedoctor/simpdf/issues>`__.

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

