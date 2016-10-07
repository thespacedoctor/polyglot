#!/usr/local/bin/python
# encoding: utf-8
"""
*Print a clean simple PDF using URL passed as argument*

:Author:
    David Young

:Date Created:
    September 28, 2015
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
import re
import codecs
from docopt import docopt
from fundamentals import tools, times
from simpdf import authenticate


import codecs
# SET ENCODE ERROR RETURN VALUE


def handler(e):
    return (u' ', e.start + 1)
codecs.register_error('dryx', handler)

###################################################################
# CLASSES                                                         #
###################################################################


class printpdf():

    """
    *The worker class for the printpdf module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``url`` -- the webpage url
        - ``title`` -- title of pdf
        - ``folderpath`` -- path at which to save pdf
        - ``append`` -- append this at the end of the file name (not title)
        - ``readability`` -- clean text with readability
    """
    # Initialisation

    def __init__(
            self,
            log,
            settings=False,
            url=False,
            title=False,
            folderpath=False,
            append=False,
            readability=True
    ):
        self.log = log
        log.debug("instansiating a new 'print' object")
        self.settings = settings
        self.url = url
        self.folderpath = folderpath
        self.title = title
        self.append = append
        self.readability = readability
        # xt-self-arg-tmpx

        # INITIAL ACTIONS
        # AUTHENTICATE AGAINST READABILITY WEBAPP PARSER CLIENT
        self.parser_client = authenticate.authenticate(
            log=self.log,
            settings=self.settings
        ).get()

        return None

    def get(self):
        """
        *get the printpdf object*

        **Return:**
            - ``pdfPath`` -- the path to the generated PDF
        """
        self.log.info('starting the ``get`` method')

        # THE ATTRIBUTES OF THE PDF
        title = self.title
        url = self.url

        # APPEND TO FILENAME?
        if self.append:
            append = self.append
        else:
            append = ""

        if not self.readability:

            # CONVERT TO PDF WITH ELECTON PDF
            from subprocess import Popen, PIPE, STDOUT
            pdfPath = self.folderpath + "/" + title + append + ".pdf"
            exe = self.settings["simpdf"]["electron path"]
            cmd = """%(exe)s -i "%(url)s" -o "%(pdfPath)s" --printBackground """ % locals()
            p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
            output = p.communicate()[0]
            print "OUTPUT: " + output
            self.log.debug('output: %(output)s' % locals())
            return pdfPath

        # PARSE THE CONTENT OF THE WEBPAGE AT THE URL
        parser_response = self.parser_client.get_article(
            self.url)
        if "503" in str(parser_response):
            return None
        article = parser_response.json()

        # GRAB THE CSS USED TO STYLE THE WEBPAGE/PDF CONTENT
        moduleDirectory = os.path.dirname(__file__)
        cssFile = moduleDirectory + "/css/main.css"
        pathToReadFile = cssFile
        readFile = codecs.open(pathToReadFile, encoding='utf-8', mode='r')
        thisCss = readFile.read()
        readFile.close()

        if "error" in article and article["error"] == True:
            print title
            print "    " + article["messages"]
            return None

        try:
            text = article["content"]
        except:
            print "Can't decode the text of %(title)s - moving on" % locals()
            return None

        # COMMON FIXES TO HTML TO RENDER CORRECTLY
        regex = re.compile(
            u'<span class="mw-editsection"><span class="mw-editsection-bracket">.*"mw-editsection-bracket">]')
        text = regex.sub(u"", text)
        regex2 = re.compile(
            u'\<sup class="noprint.*better source needed\<\/span\>\<\/a\>\<\/i\>\]\<\/sup\>', re.I)
        text = regex2.sub(u"", text)
        regex2 = re.compile(
            u'\<a href="https\:\/\/en\.wikipedia\.org\/wiki\/.*(\#.*)"\>\<span class=\"tocnumber\"\>', re.I)
        text = regex2.sub(u'<a href="\g<1>"><span class="tocnumber">', text)

        # GRAB HTML TITLE IF NOT SET IN ARGUMENTS
        if title == False:
            title = article["title"].encode("utf-8", "ignore")
            title = title.decode("utf-8")
            title = title.encode("ascii", "ignore")
        rstrings = """:/"&\\'"""
        for i in rstrings:
            title = title.replace(i, "")

        # USE DATETIME IF TITLE STILL NOT SET
        if len(title) == 0:
            from datetime import datetime, date, time
            now = datetime.now()
            title = now.strftime("%Y%m%dt%H%M%S")

        # REGENERATE THE HTML DOCUMENT WITH CUSTOM STYLE
        filePath = self.folderpath + "/" + title + append + ".html"
        writeFile = codecs.open(
            filePath, encoding='utf-8', mode='w')
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

        # CONVERT TO PDF WITH ELECTON PDF
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


if __name__ == '__main__':
    main()
