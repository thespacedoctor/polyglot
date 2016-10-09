Usage
======

.. code-block:: bash 
   
    
    Documentation for polyglot can be found here: http://pypolyglot.readthedocs.org/en/stable
    
    Translate documents and webpages to various markup languages and document formats (html, epub, mobi ..)
    
    Usage:
        polyglot init
        polyglot [-oc] (pdf|html) <url> [<destinationFolder> -f <filename> -s <pathToSettingsFile>]
    
    Options:
        init                  setup the polyglot settings file for the first time
        pdf                   print webpage to pdf
        html                  parse and download webpage to a local HTML document
    
        -h, --help                                                      show this help message
        -v, --version                                                   show version
        -o, --open                                                      open the document after creation
        -c, --clean                                                     add polyglot's clean styling to the output document
        <url>                                                           the url of the article's webpage
        -s <pathToSettingsFile>, --settings <pathToSettingsFile>        path to alternative settings file (optional)
        <destinationFolder>                                             the folder to save the parsed PDF or HTML document to (optional)
        -f <filename>, --filename <filename>                            the name of the file to save, otherwise use webpage title as filename (optional)
    
