#!/usr/local/bin/python
# encoding: utf-8
"""
printpdf.py
===========
:Summary:
    Print a clean simple PDF using URL passed as argument

:Author:
    David Young

:Date Created:
    September 28, 2015

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
import re
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from simpdf import authenticate


###################################################################
# CLASSES                                                         #
###################################################################
class printpdf():

    """
    The worker class for the printpdf module

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``url`` -- toe webpage url
        - ``title`` -- title of pdf
        - ``folderpath`` -- path at which to save pdf


    **Todo**
        - @review: when complete, clean printpdf class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            settings=False,
            url=False,
            title=False,
            folderpath=False
    ):
        self.log = log
        log.debug("instansiating a new 'print' object")
        self.settings = settings
        self.url = url
        self.folderpath = folderpath
        self.title = title
        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions
        self.parser_client = authenticate.authenticate(
            log=self.log,
            settings=self.settings
        ).get()

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the printpdf object

        **Return:**
            - ``printpdf``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        title = self.title

        printpdf = None
        url = self.url

        parser_response = self.parser_client.get_article(
            self.url)
        article = parser_response.json()

        moduleDirectory = os.path.dirname(__file__)
        cssFile = moduleDirectory + "/css/main.css"
        import codecs
        pathToReadFile = cssFile
        readFile = codecs.open(pathToReadFile, encoding='utf-8', mode='r')
        thisCss = readFile.read()
        readFile.close()

        # RECODE INTO ASCII
        # udata=thisData.decode("utf-8")
        # thisData=udata.encode("ascii","ignore")

        import codecs

        try:
            text = article["content"]
        except:
            print "Can't decode the text of %(title)s - moving on" % locals()
            return None

        regex = re.compile(
            u'<span class="mw-editsection"><span class="mw-editsection-bracket">.*"mw-editsection-bracket">]')
        text = regex.sub(u"", text)
        regex2 = re.compile(
            u'\<sup class="noprint.*better source needed\<\/span\>\<\/a\>\<\/i\>\]\<\/sup\>', re.I)
        text = regex2.sub(u"", text)
        regex2 = re.compile(
            u'\<a href="https\:\/\/en\.wikipedia\.org\/wiki\/.*(\#.*)"\>\<span class=\"tocnumber\"\>', re.I)
        text = regex2.sub(u'<a href="\g<1>"><span class="tocnumber">', text)
        # RECODE INTO ASCII
        if title == False:
            title = article["title"].encode("utf-8", "ignore")
            title = title.decode("utf-8")
            title = title.encode("ascii", "ignore")
        rstrings = """:/"&\\'"""
        for i in rstrings:
            title = title.replace(i, "")

        if len(title) == 0:
            from datetime import datetime, date, time
            now = datetime.now()
            title = now.strftime("%Y%m%dt%H%M%S")

        filePath = self.folderpath + "/" + title + ".html"
        writeFile = codecs.open(
            self.folderpath + "/" + title + ".html", encoding='utf-8', mode='w')
        content = u"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>%(title)s</title>

<link rel="stylesheet" type="text/css" href="%(cssFile)s" />



</head>
<body>

<h1>%(title)s</h1>
<a href="%(url)s">original source</a>
</br></br>


%(text)s 
</body>
</html>""" % locals()
        writeFile.write(content)
        writeFile.close()

        print filePath

        from subprocess import Popen, PIPE, STDOUT
        pdfPath = filePath.replace(".html", ".pdf")
        exe = self.settings["simpdf"]["electron path"]
        cmd = """%(exe)s -i "%(filePath)s" -o "%(pdfPath)s" """ % locals()
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        print "OUTPUT: " + output
        self.log.debug('output: %(output)s' % locals())

        # REMOVE HTML FILE
        os.remove(filePath)

        self.log.info('completed the ``get`` method')
        return pdfPath
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx

# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
