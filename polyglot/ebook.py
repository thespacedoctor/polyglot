#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert various document formats to epub or mobi*

:Author:
    David Young

:Date Created:
    October  9, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import shutil
os.environ['TERM'] = 'vt100'
from fundamentals import tools
import codecs
from subprocess import Popen, PIPE
from datetime import datetime, date, time


class ebook():
    """
    *The worker class for the ebook module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``urlOrPath`` -- the url or path to the content source
        - ``bookFormat`` -- the output format (epub, mobi)
        - ``outputDirectory`` -- path to the directory to save the output html file to.
        - ``title`` -- the title of the output document. I. False then use the title of the original source. Default *False*
        - ``header`` -- content to add before the article/book content in the resulting ebook. Default *False*
        - ``footer`` -- content to add at the end of the article/book content in the resulting ebook. Default *False*

    **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage
            - update the package tutorial if needed

        **WebToEpub**

        To generate an ebook from an article found on the web, using the webpages's title as the filename for the book:

        .. code-block:: python

            from polyglot import ebook
            epub = ebook(
                log=log,
                settings=settings,
                urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
                title=False,
                bookFormat="epub",
                outputDirectory="/path/to/output/folder"
            )
            pathToEpub = epub.get()

        To add a header and footer to the epub book, and specify the title/filename for the book:

        .. code-block:: python

            from polyglot import ebook
            epub = ebook(
                log=log,
                settings=settings,
                urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
                title="MySQL Sucker",
                bookFormat="epub",
                outputDirectory="/path/to/output/folder",
                header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
                footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
            )
            pathToEpub = epub.get()

        **WebToMobi**

        To generate a mobi version of the webarticle, just switch *epub* for *mobi*:

        .. code-block:: python

            from polyglot import ebook
            mobi = ebook(
                log=log,
                settings=settings,
                urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
                title="MySQL Sucker",
                bookFormat="mobi",
                outputDirectory="/path/to/output/folder",
                header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
                footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
            )
            pathToMobi = mobi.get()

        **DocxToEpub**

        To instead convert a DOCX document to epub, simply switch out the URL for the path to the DOCX file, like so:

        .. code-block:: python


            from polyglot import ebook
            epub = ebook(
                log=log,
                settings=settings,
                urlOrPath="/path/to/Volkswagen.docx",
                title="A book about a car",
                bookFormat="epub",
                outputDirectory="/path/to/output/folder",
                header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
                footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
            )
            pathToEpub = epub.get()

        **DocxToMobi**

        You can work it out yourself by now!
    """
    # Initialisation

    def __init__(
            self,
            log,
            settings,
            urlOrPath,
            outputDirectory,
            bookFormat,
            title=False,
            header=False,
            footer=False
    ):
        self.log = log
        log.debug("instansiating a new 'ebook' object")
        self.settings = settings
        self.title = title
        self.header = header
        self.footer = footer
        self.urlOrPath = urlOrPath
        self.outputDirectory = outputDirectory
        self.format = bookFormat
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def get(self):
        """
        *get the ebook object*

        **Return:**
            - ``ebook``

        **Usage:**

            See class docstring for usage
        """
        self.log.info('starting the ``get`` method')

        if self.format == "epub":
            if self.urlOrPath[:4] == "http" or self.urlOrPath[:4] == "www.":
                ebook = self._url_to_epub()
            elif ".docx" in self.urlOrPath:
                ebook = self._docx_to_epub()

        if self.format == "mobi":
            if self.urlOrPath[:4] == "http" or self.urlOrPath[:4] == "www.":
                epub = self._url_to_epub()
            elif ".docx" in self.urlOrPath:
                epub = self._docx_to_epub()

            if not epub:
                return None

            ebook = self._epub_to_mobi(
                epubPath=epub,
                deleteEpub=False
            )

        self.log.info('completed the ``get`` method')
        return ebook

    def _url_to_epub(
            self):
        """*generate the epub book from a URL*
        """
        self.log.info('starting the ``_url_to_epub`` method')

        from polyglot import htmlCleaner
        cleaner = htmlCleaner(
            log=self.log,
            settings=self.settings,
            url=self.urlOrPath,
            outputDirectory=self.outputDirectory,
            title=self.title,  # SET TO FALSE TO USE WEBPAGE TITLE,
            style=False,  # add simpdf's styling to the HTML document
            metadata=True,  # include metadata in generated HTML (e.g. title),
            h1=False  # include title as H1 at the top of the doc
        )
        html = cleaner.clean()

        if not html:
            return None

        if self.footer:
            footer = self._tmp_html_file(self.footer)
            footer = '"%(footer)s"' % locals()
        else:
            footer = ""

        if self.header:
            header = self._tmp_html_file(self.header)
            header = '"%(header)s"' % locals()
        else:
            header = ""

        # HTML SOURCE FILE
        epub = html.replace(".html", ".epub")
        pandoc = self.settings["executables"]["pandoc"]

        cmd = """%(pandoc)s -S -s -f html -t epub3 %(header)s "%(html)s" %(footer)s -o "%(epub)s" """ % locals(
        )
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        self.log.debug('output: %(stdout)s' % locals())

        try:
            with open(epub):
                pass
            fileExists = True
        except IOError:
            fileExists = False
            raise IOError(
                "the epub %s does not exist on this machine, here is the failure message: %s" % (epub, stderr))

        os.remove(html)

        self.log.info('completed the ``_url_to_epub`` method')
        return epub

    def _tmp_html_file(
            self,
            content):
        """*create a tmp html file with some content used for the header or footer of the ebook*

        **Key Arguments:**
            - ``content`` -- the content to include in the HTML file.
        """
        self.log.info('starting the ``_tmp_html_file`` method')

        content = """

<hr>
<div style="text-align: center">
%(content)s
</div>
<hr>

""" % locals()

        now = datetime.now()
        now = now.strftime("%Y%m%dt%H%M%S%f")
        pathToWriteFile = "/tmp/%(now)s.html" % locals()
        try:
            self.log.debug("attempting to open the file %s" %
                           (pathToWriteFile,))
            writeFile = codecs.open(
                pathToWriteFile, encoding='utf-8', mode='w')
        except IOError, e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            self.log.critical(message)
            raise IOError(message)
        writeFile.write(content)
        writeFile.close()

        self.log.info('completed the ``_tmp_html_file`` method')
        return pathToWriteFile

    def _epub_to_mobi(
            self,
            epubPath,
            deleteEpub=False):
        """*convert the give epub to mobi format using kindlegen*

        **Key Arguments:**
            - ``epubPath`` -- path to the epub book
            - ``deleteEpub`` -- delete the epub when mobi is generated. Default *False*

        **Return:**
            - ``mobi`` -- the path to the generated mobi book
        """
        self.log.info('starting the ``_epub_to_mobi`` method')

        mobi = epubPath.replace(".epub", ".mobi")
        kindlegen = self.settings["executables"]["kindlegen"]
        cmd = """%(kindlegen)s "%(epubPath)s" """ % locals(
        )
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        self.log.debug('output: %(stdout)s' % locals())

        try:
            with open(mobi):
                pass
            fileExists = True
        except IOError:
            fileExists = False
            self.log.error(
                "the mobi %s does not exist on this machine. The kindlegen error was: %s" % (mobi, stdout))
            return False

        if deleteEpub:
            os.remove(epubPath)

        self.log.info('completed the ``_epub_to_mobi`` method')
        return mobi

    def _docx_to_epub(
            self):
        """*convert docx file to epub*
        """
        self.log.info('starting the ``_docx_to_epub`` method')

        if self.footer:
            footer = self._tmp_html_file(self.footer)
            footer = '"%(footer)s"' % locals()
        else:
            footer = ""

        if self.header:
            header = self._tmp_html_file(self.header)
            header = '"%(header)s"' % locals()
        else:
            header = ""

        # FIRST CONVERT THE DOC TO HTML
        docx = self.urlOrPath

        if self.title:
            title = self.title.replace(".html", "")
            html = "/tmp/" + self.title.replace(".html", "") + ".html"
        else:
            title = os.path.basename(docx).replace(
                ".docx", "").replace("_", " ")
            html = "/tmp/" + os.path.basename(docx).replace(".docx", ".html")
        pandoc = self.settings["executables"]["pandoc"]

        # TMP IMAGE DIR
        now = datetime.now()
        now = now.strftime("%Y%m%dt%H%M%S")
        imageDir = "/tmp/%(now)s" % locals()
        if not os.path.exists(imageDir):
            os.makedirs(imageDir)
        cmd = """%(pandoc)s --extract-media=%(imageDir)s -t html -f docx "%(docx)s" -o "%(html)s" """ % locals()
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        self.log.debug('output: %(stdout)s' % locals())

        try:
            with open(html):
                pass
            fileExists = True
        except IOError:
            fileExists = False
            self.log.error(
                "the html %s does not exist on this machine, here is the failure message: %s" % (html, stderr))
            try:
                shutil.rmtree(imageDir)
            except:
                pass
            return None

        if fileExists:
            if self.outputDirectory:
                epub = self.outputDirectory + "/" + \
                    os.path.basename(html).replace(".html", ".epub")
            else:
                epub = docx.replace(".docx", ".epub")
            pandoc = self.settings["executables"]["pandoc"]

            cmd = """%(pandoc)s --metadata=title:"%(title)s" -S -s -f html -t epub3 %(header)s "%(html)s" %(footer)s -o "%(epub)s" """ % locals(
            )
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
            stdout, stderr = p.communicate()
            self.log.debug('output: %(stdout)s' % locals())

            try:
                shutil.rmtree(imageDir)
                os.remove(html)
            except:
                pass

            try:
                with open(epub):
                    pass
                fileExists = True
            except IOError:
                fileExists = False
                self.log.error(
                    "the epub %s does not exist on this machine, here is the failure message: %s" % (epub, stderr))
                return None

        self.log.info('completed the ``_docx_to_epub`` method')
        return epub

    # use the tab-trigger below for new method
    # xt-class-method
