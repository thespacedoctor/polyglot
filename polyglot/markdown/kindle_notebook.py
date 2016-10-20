#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert the HTML export of kindle notebooks (from kindle apps) to markdown*

:Author:
    David Young

:Date Created:
    October 17, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import collections
os.environ['TERM'] = 'vt100'
from fundamentals import tools

# THESE ARE THE 4 KINDLE COLORS ARE HOW THEY TRANSLATE TO MD
colorCode = {
    "blue": "code",
    "yellow": "text",
    "orange": "quote",
    "pink": "header"
}


class kindle_notebook():
    """
    *convert the HTML export of kindle notebooks (from kindle apps) to markdown*

    **Key Arguments:**
        - ``log`` -- logger
        - ``kindleExportPath`` -- path to the exported kindle HTML file
        - ``outputPath`` -- the output path to the md file.

    **Usage:**

        To convert the exported HTML file of annotation and notes from a kindle book or document to markdown, run the code:

        .. code-block:: python 

            from polyglot.markdown import kindle_notebook
            nb = kindle_notebook(
                log=log,
                kindleExportPath="/path/to/kindle_export.html",
                outputPath="/path/to/coverted_annotations.md"
            )
            nb.convert()

        The colours of the annotations convert to markdown attributes via the following key:

        .. code-block: json

            colorCode = {
                "blue": "code",
                "yellow": "text",
                "orange": "quote",
                "pink": "header"
            }
    """
    # Initialisation

    def __init__(
            self,
            log,
            kindleExportPath,
            outputPath
    ):
        self.log = log
        log.debug("instansiating a new 'kindle_notebook' object")
        self.kindleExportPath = kindleExportPath
        self.outputPath = outputPath

        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def convert(self):
        """
        *convert the kindle_notebook object*

        **Return:**
            - ``kindle_notebook``

        **Usage:**
        .. todo::

            - add usage info
            - create a sublime snippet for usage
            - update the package tutorial if needed

        .. code-block:: python 

            usage code 
        """
        self.log.info('starting the ``convert`` method')

        import codecs
        pathToReadFile = self.kindleExportPath
        try:
            self.log.debug("attempting to open the file %s" %
                           (pathToReadFile,))
            readFile = codecs.open(pathToReadFile, encoding='utf-8', mode='r')
            annotations = readFile.read()
            readFile.close()
        except IOError, e:
            message = 'could not open the file %s' % (pathToReadFile,)
            self.log.critical(message)
            raise IOError(message)

        annotations = annotations.replace(u"’", "'").replace(
            u"“ ", '"').replace(u"“", '"').replace(u"”", '"').replace(u"–", "-").replace(u"—", "-")

        # COLLECT KEY COMPONENTS
        try:
            title = self.find_component("bookTitle", annotations)
        except:
            return False
        regex = re.compile(r'_xx\d*xx$')
        title = regex.sub("", title)
        authors = self.find_component("authors", annotations)
        citation = self.find_component("citation", annotations)

        # CLEAN THE CITATION
        regex = re.compile(r'</?i>', re.S)
        citation = regex.sub('*', citation)
        regex = re.compile(r'Citation \(.*?\): ', re.S)
        citation = regex.sub('', citation).replace(" Kindle edition.", "")

        # COLLECT ANNOTATIONS
        annotationDict = {}
        matchObject = re.finditer(
            r"""<div class="noteHeading">\s+Highlight\(<span.*?>(?P<color>.*?)</span>\)((?P<section>.*?)Page (?P<page>\d+))?.*?Location (?P<location>\d+)\s+</div>\s+<div class="noteText">(?P<note>.*?)</div>""",
            annotations,
            flags=re.S
        )

        for match in matchObject:
            location = int(match.group("location"))
            location = "%(location)09d" % locals()
            if match.group("page"):
                try:
                    annotationDict[location] = {"color": match.group("color"), "page": match.group(
                        "page"), "section": self.clean(match.group("section"))[3:-2], "note": self.clean(match.group("note"))}
                except:
                    print match.group("note")
                    sys.exit(0)
            else:
                try:
                    annotationDict[location] = {"color": match.group(
                        "color"), "note": self.clean(match.group("note"))}
                except:
                    print match.group("note")
                    sys.exit(0)

        # COLLECT PERSONAL NOTES
        matchObject = re.finditer(
            r"""<div class="noteHeading">\s+Note -( Page (?P<page>\d+))?.*?Location (?P<location>\d+)\s+</div>\s+<div class="noteText">(?P<note>.*?)</div>""",
            annotations,
            flags=re.S
        )

        for match in matchObject:
            location = int(match.group("location"))
            location = "%(location)09dnote" % locals()
            if match.group("page"):
                annotationDict[location] = {"color": None, "page": match.group(
                    "page"), "note": self.clean(match.group("note"))}
            else:
                annotationDict[location] = {
                    "color": None, "note": self.clean(match.group("note"))}

        annotationDict = collections.OrderedDict(
            sorted(annotationDict.items()))

        mdContent = "\n# %(title)s\n\nAuthors: **%(authors)s**\n\n" % locals()
        for k, v in annotationDict.iteritems():
            mdContent += self.convertToMD(v) + "\n\n"

        if len(annotationDict) == 0:
            return False

        pathToWriteFile = self.outputPath
        try:
            self.log.debug("attempting to open the file %s" %
                           (pathToWriteFile,))
            writeFile = codecs.open(
                pathToWriteFile, encoding='utf-8', mode='w')
        except IOError, e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            self.log.critical(message)
            raise IOError(message)
        writeFile.write(mdContent)
        writeFile.close()

        self.log.info('completed the ``convert`` method')
        return pathToWriteFile

    def clean(self, text):
        return text.strip().replace(u"’", "'").replace(u"“ ", '"').replace(u"“", '"').replace(u"”", '"').replace(u"–", "-").replace(u"—", "-")

    def find_component(self, divtag, annotations):
        component = re.search(
            r"""<div class="%(divtag)s">(.*?)</div>""" % locals(), annotations, re.S)

        return self.clean(component.group(1))

    def convertToMD(self, kindleNote):
        if kindleNote["color"] == None:
            return "**NOTE**\n: " + kindleNote["note"].replace("\n", " ")
        mdType = colorCode[kindleNote["color"]]
        if mdType == "code":
            return "```\n" + kindleNote["note"] + "\n```"
        elif mdType == "text":
            return kindleNote["note"]
        elif mdType == "header":
            regex = re.compile(r'_xx\d*xx$')
            kindleNote["note"] = regex.sub("", kindleNote["note"])
            return "## " + kindleNote["note"].replace("\n", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
        elif mdType == "quote":
            return "> " + kindleNote["note"].replace("\n", "> ")

    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
