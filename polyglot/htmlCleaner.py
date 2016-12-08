#!/usr/local/bin/python
# encoding: utf-8
"""
*using the Mercury Parser API to clean up a local html file*

:Author:
    David Young

:Date Created:
    October  1, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import codecs
import re
os.environ['TERM'] = 'vt100'
from fundamentals import tools
import requests


class htmlCleaner():
    """
    *A parser/cleaner to strip a webpage article of all cruft and neatly present it with some nice css*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``url`` -- the URL to the HTML page to parse and clean
        - ``outputDirectory`` -- path to the directory to save the output html file to
        - ``title`` -- title of the document to save. If *False* will take the title of the HTML page as the filename. Default *False*.
        - ``style`` -- add polyglot's styling to the HTML document. Default *True*
        - ``metadata`` -- include metadata in generated HTML. Default *True*
        - ``h1`` -- include title as H1 at the top of the doc. Default *True*

    **Usage:**

        To generate the HTML page, using the title of the webpage as the filename:

        .. code-block:: python 

            from polyglot import htmlCleaner
            cleaner = htmlCleaner(
                log=log,
                settings=settings,
                url="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
                outputDirectory="/tmp"
            )
            cleaner.clean()  

        Or specify the title of the document and remove styling, metadata and title:

        .. code-block:: python 

            from polyglot import htmlCleaner
            cleaner = htmlCleaner(
                log=log,
                settings=settings,
                url="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
                outputDirectory="/tmp",
                title="my_clean_doc",
                style=False,
                metadata=False,
                h1=False
            )
            cleaner.clean() 

    """
    # INITIALISATION

    def __init__(
            self,
            log,
            settings,
            url,
            outputDirectory=False,
            title=False,
            style=True,
            metadata=True,
            h1=True
    ):
        self.log = log
        log.debug("instansiating a new 'htmlCleaner' object")
        self.settings = settings
        self.url = url
        self.outputDirectory = outputDirectory
        self.title = title
        self.style = style
        self.metadata = metadata
        self.h1 = h1

        # INITIAL ACTIONS

        return None

    def clean(
            self):
        """*parse and clean the html document with Mercury Parser*

        **Return:**
            - ``filePath`` -- path to the cleaned HTML document

        **Usage:**

            See class usage 
        """
        self.log.info('starting the ``clean`` method')

        url = self.url

        # PARSE THE CONTENT OF THE WEBPAGE AT THE URL

        parser_response = self._request_parsed_article_from_mercury(url)
        if "503" in str(parser_response):
            return None
        article = parser_response.json()

        # GRAB THE CSS USED TO STYLE THE WEBPAGE/PDF CONTENT
        if self.style:
            moduleDirectory = os.path.dirname(__file__)
            cssFile = moduleDirectory + "/css/main.css"
            pathToReadFile = cssFile
            readFile = codecs.open(pathToReadFile, encoding='utf-8', mode='r')
            thisCss = readFile.read()
            readFile.close()
        else:
            thisCss = ""

        # CATCH ERRORS
        if "error" in article and article["error"] == True:
            print url
            print "    " + article["messages"]
            return None
        try:
            text = article["content"]
        except:
            print "Can't decode the text of %(url)s - moving on" % locals()
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
        regex = re.compile(
            u'srcset=".*?">')
        text = regex.sub(u"", text)

        # GRAB HTML TITLE IF NOT SET IN ARGUMENTS
        if self.title == False:
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
            self.title = title

        title = self.title.replace(".html", "")
        pageTitle = title.replace("_", " ")

        # REGENERATE THE HTML DOCUMENT WITH CUSTOM STYLE
        filePath = self.outputDirectory + "/" + title + ".html"
        writeFile = codecs.open(
            filePath, encoding='utf-8', mode='w')
        if self.metadata:
            metadata = "<title>%(title)s</title>" % locals()
        else:
            metadata = ""

        if self.h1:
            h1 = "<h1>%(pageTitle)s</h1>" % locals()
        else:
            h1 = ""
        content = u"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
%(metadata)s 

<style>
%(thisCss)s
</style>

</head>
<body>

%(h1)s 
<a href="%(url)s">original source</a>
</br></br>


%(text)s 
</body>
</html>""" % locals()
        writeFile.write(content)
        writeFile.close()

        self.log.info('completed the ``clean`` method')
        return filePath

    def _request_parsed_article_from_mercury(
            self,
            url):
        """* request parsed article from mercury*

        **Key Arguments:**
            - ``url`` -- the URL to the HTML page to parse and clean

        **Return:**
            - None

        **Usage:**
            ..  todo::

                - add usage info
                - create a sublime snippet for usage
                - update package tutorial if needed

            .. code-block:: python 

                usage code 

        """
        self.log.info(
            'starting the ``_request_parsed_article_from_mercury`` method')

        try:
            response = requests.get(
                url="https://mercury.postlight.com/parser",
                params={
                    "url": url,
                },
                headers={
                    "x-api-key": self.settings["mercury api key"],
                },
            )

        except requests.exceptions.RequestException:
            print('HTTP Request failed')

        self.log.info(
            'completed the ``_request_parsed_article_from_mercury`` method')
        return response

    # use the tab-trigger below for new method
    # xt-class-method
