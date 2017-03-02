#!/usr/local/bin/python
# encoding: utf-8
"""
*convert plain-text blocks into various markdown elements*

:Author:
    David Young

:Date Created:
    February 26, 2017
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
os.environ['TERM'] = 'vt100'
from fundamentals import tools
from datetime import datetime, date, time
from random import randint


class translate():
    """
    *The Multimarkdown translator object*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Usage:**

        To setup your logger, settings and database connections, please use the ``fundamentals`` package (`see tutorial here <http://fundamentals.readthedocs.io/en/latest/#tutorial>`_).

        To initiate a ``translate`` object, use the following:

        .. code-block:: python

            from polyglot.markdown import translate
            md = translate(
                log=log,
                settings=settings
            )
    """
    # Initialisation

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'translate' object")
        self.settings = settings
        self.reWS = re.compile(r'^(\s*)(\S.*?)(\s*)$', re.S)
        # xt-self-arg-tmpx
        return None

    def bold(
            self,
            text):
        """*convert plain-text to MMD bolded text*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD bold

        **Return:**
            - ``text`` -- the bolded text

        **Usage:**

            To convert a text block to bolded text:

            .. code-block:: python

                text = md.bold(" nice day!   ")
                print text

                # OUTPUT:  **nice day!**
        """
        return self._surround(text, "**", "**")

    def em(
            self,
            text):
        """*convert plain-text to MMD italicised text*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD italics

        **Return:**
            - ``text`` -- the emphasised text

        **Usage:**

            To convert a text block to emphasised text:

            .. code-block:: python

                text = md.em(" nice day!   ")
                print text

                # OUTPUT:  _nice day!_
        """
        return self._surround(text, "_", "_")

    def underline(
            self,
            text):
        """*convert plain-text to HTML underline text*

        **Key Arguments:**
            - ``text`` -- the text to convert to HTML underlined

        **Return:**
            - ``text`` -- the underlined text

        **Usage:**

            To convert a text block to underlined text:

            .. code-block:: python

                text = md.underline(" nice day!   ")
                print text

                # OUTPUT:  <u>nice day!</u>
        """
        return self._surround(text, "<u>", "</u>")

    def strike(
            self,
            text):
        """*convert plain-text to HTML strike-through text*

        **Key Arguments:**
            - ``text`` -- the text to convert to HTML strike-through

        **Return:**
            - ``text`` -- the strike-through text

        **Usage:**

            To convert a text block to strike-through text:

            .. code-block:: python

                text = md.strike(" nice day!   ")
                print text

                # OUTPUT:  <s>nice day!</s>
        """
        return self._surround(text, "<s>", "</s>")

    def hl(
            self,
            text):
        """*convert plain-text to MMD critical markup highlighted text*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD highlighted text

        **Return:**
            - ``text`` -- the highlighted text

        **Usage:**

            To convert a text block to highlighted text:

            .. code-block:: python

                text = md.hl(" nice day!   ")
                print text

                # OUTPUT:  {==nice day!==}
        """
        return self._surround(text, "{==", "==}")

    def code(
            self,
            text):
        """*convert plain-text to MMD inline-code text*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD inline-code text

        **Return:**
            - ``text`` -- the inline-code text

        **Usage:**

            To convert a text block to inline-code text:

            .. code-block:: python

                text = md.code(" nice day!   ")
                print text

                # OUTPUT:  `nice day!`
        """
        return self._surround(text, "`", "`")

    def comment(
            self,
            text):
        """*convert plain-text to MMD comment*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD comment

        **Return:**
            - ``text`` -- the comment text

        **Usage:**

            To convert a text block to comment text:

            .. code-block:: python

                text = md.comment(" nice day!   ")
                print text

                # OUTPUT:  {>>nice day!<<}
        """
        return self._surround(text, "{>>", "<<}")

    def footnote(
            self,
            text):
        """*convert plain-text to MMD footnote*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD footnote

        **Return:**
            - ``text`` -- the footnote text

        **Usage:**

            To convert a text block to footnote text:

            .. code-block:: python

                text = md.footnote(" nice day!   ")
                print text

                # OUTPUT:  [^20170228T21:57:40-99]
                #
                # [^20170228T21:57:40-99]: nice day!
        """

        rand = str(randint(0, 99))
        now = datetime.now()
        now = now.strftime("%Y%m%dT%H:%M:%S-") + rand
        text = text.strip()
        regex = re.compile(r'\n(\S)')
        text = regex.sub("\n    \g<1>", text)

        return "[^%(now)s]\n\n[^%(now)s]: %(text)s\n\n" % locals()

    def glossary(
            self,
            term,
            definition):
        """*genarate a MMD glossary*

        **Key Arguments:**
            - ``term`` -- the term to add as a glossary item
            - ``definition`` -- the definition of the glossary term

        **Return:**
            - ``glossary`` -- the glossary text

        **Usage:**

            To genarate a glossary item:

            .. code-block:: python

                text = \"\"\"Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
                Also the makers of really great products.\"\"\"

                definition = md.glossary("Apple", text)
                print definition

                # OUTPUT: 
                # [^apple]
                #
                # [^apple]: Apple
                #    Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
                #    Also the makers of really great products.
        """
        term = term.strip()
        term = term.lower()
        title = term.title()
        definition = definition.strip()
        regex = re.compile(r'\n(\S)')
        definition = regex.sub("\n    \g<1>", definition)

        return "[^%(term)s]\n\n[^%(term)s]: %(title)s\n    %(definition)s" % locals()

    def cite(
            self,
            title,
            author=False,
            year=False,
            url=False,
            publisher=False,
            mediaKind=False,
            linkedText=False,
            nocite=False):
        """*generate a MMD citation*

        **Key Arguments:**
            - ``title`` -- the citation title
            - ``author`` -- the author. Dafault *False*
            - ``year`` -- year published. Dafault *False*
            - ``url`` -- url to the media. Dafault *False*
            - ``publisher`` -- the publisher of the media. Dafault *False*
            - ``mediaKind`` -- what kind of media is it?. Dafault *False*
            - ``linkedText`` -- the text to link to the citation. Dafault *False/blank*
            - ``nocite`` -- a give citation that has no reference in main doc

        **Return:**
            - ``citation`` -- the MMD citation

        **Usage:**

            To generate a MMD citation:

            .. code-block:: python

                citation = md.cite(
                    title="A very good book",
                    author="John Doe",
                    year=2015,
                    url="http://www.thespacedoctor.co.uk",
                    publisher="Beefy Books",
                    mediaKind=False,
                    linkedText="Doe 2015")
                print citation

                # OUTPUT:  [Doe 2015][#averygoodbook90]
                #
                # [#averygoodbook90]: John Doe. *[A Very Good Book](http://www.thespacedoctor.co.uk)*. Beefy Books, 2015. 
        """

        rand = str(randint(0, 100))
        anchor = title.replace(" ", "").lower()
        title = title.title()

        citation = ""
        if author:
            author = author.title() + ". "
        else:
            author = ""

        if title[-1] == ".":
            title = title[:-1]

        if url:
            title = "*[%(title)s](%(url)s)*. " % locals()
        else:
            title = "*%(title)s*." % locals()

        if publisher and year:
            publisher = "%(publisher)s, %(year)s. " % locals()
        elif publisher:
            publisher = "%(publisher)s. " % locals()
        elif year:
            publisher = "%(year)s. " % locals()
        else:
            publisher = ""

        if mediaKind:
            mediaKind = "(%(mediaKind)s) " % locals()
            mediaKind = mediaKind.lower()
        else:
            mediaKind = ""

        if not linkedText:
            linkedText = ""

        if nocite:
            linkedText = "Not Cited"

        return "[%(linkedText)s][#%(anchor)s%(rand)s]\n\n[#%(anchor)s%(rand)s]: %(author)s%(title)s%(publisher)s%(mediaKind)s" % locals()

    def url(
            self,
            text):
        """*convert plain-text to MMD clickable URL*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD clickable URL

        **Return:**
            - ``text`` -- the URL text

        **Usage:**

            To convert a text block to MMD clickable URL:

            .. code-block:: python

                text = md.url(" http://www.google.com    ")
                print text

                # OUTPUT:  <http://www.google.com>
        """
        return self._surround(text, "<", ">")

    def math_inline(
            self,
            text):
        """*convert plain-text to MMD inline math*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD inline math

        **Return:**
            - ``math`` -- the inline math text

        **Usage:**

            To convert a text to MMD inline math:

            .. code-block:: python

                text = md.math_inline("{e}^{i\pi }+1=0")
                print text

                # OUTPUT:  ${e}^{i\pi }+1=0$
        """
        return self._surround(text, "$", "$")

    def math_block(
            self,
            text):
        """*convert plain-text to MMD math block*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD math block

        **Return:**
            - ``math`` -- the math block text

        **Usage:**

            To convert a text to MMD math block:

            .. code-block:: python

                text = md.math_inline("{e}^{i\pi }+1=0")
                print text

                # OUTPUT:  $${e}^{i\pi }+1=0$$
        """
        return self._surround(text, "\n\n$$", "$$\n\n")

    def header(
            self,
            text,
            level):
        """*convert plain-text to MMD header*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD header
            - ``level`` -- the header level to convert the text to

        **Return:**
            - ``header`` -- the MMD header

        **Usage:**

            To convert a text MMD header:

            .. code-block:: python

                header = md.header(" This is my header  ", level=3)
                print header

                # OUTPUT:
                # ### This is my header
                #
        """
        m = self.reWS.match(text)

        prefix = m.group(1)
        text = m.group(2)
        suffix = m.group(3)

        return "#" * level + " %(text)s  \n" % locals()

    def definition(
            self,
            text,
            definition):
        """*genarate a MMD definition*

        **Key Arguments:**
            - ``text`` -- the text to define
            - ``definition`` -- the definition

        **Return:**
            - ``definition`` -- the MMD style definition

        **Usage:**

            To genarate a MMD definition:

            .. code-block:: python

                text = \"\"\"Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
                Also the makers of really great products.\"\"\"

                definition = md.definition("Apple", text)
                print definition

                # OUTPUT:
                # Apple
                # :    Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
                #      Also the makers of really great products.
                #
        """
        text = text.strip()
        definition = definition.strip()
        regex = re.compile(r'\n(\S)')
        definition = regex.sub("\n    \g<1>", definition)

        return "%(text)s\n:    %(definition)s" % locals()

    def headerLink(
            self,
            headerText,
            text=False):
        """*generate a link to a MMD header*

        **Key Arguments:**
            - ``headerText`` -- the header text (or anchor tag)
            - ``text`` -- the doc text to link. Default *False*

        **Return:**
            - ``link`` -- the link to the header

        **Usage:**

            To generate a MMD header link:

            .. code-block:: python

                link = md.headerLink(" This is my header  ", "inline text")
                print link

                # OUTPUT:
                # [inline text][This is my header]
                #
        """
        headerText = headerText.strip()

        if text:
            return self._surround(text, "[", "][%(headerText)s]" % locals())
        else:
            return "[%(headerText)s][]" % locals()

    def image(
            self,
            url,
            title="",
            width=800):
        """*create MMD image link*

        **Key Arguments:**
            - ``title`` -- the title for the image
            - ``url`` -- the image URL
            - ``width`` -- the width in pixels of the image. Default *800*

        **Return:**
            - ``imageLink`` -- the MMD image link

        **Usage:**

            To create a MMD image link:

            .. code-block:: python

                imageLink = md.image(
                    "http://www.thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png", "thespacedoctor icon", 400)
                print imageLink

                # OUTPUT:
                # ![thespacedoctor icon][thespacedoctor icon 20170228t130146.472262]
                #
                # [thespacedoctor icon 20170228t130146.472262]: http://www.thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png "thespacedoctor icon" width=400px
                #
        """
        title = title.strip()
        caption = title

        now = datetime.now()
        figId = now.strftime("%Y%m%dt%H%M%S.%f")

        if len(title):
            figId = "%(title)s %(figId)s" % locals()

        imageLink = """\n\n![%(caption)s][%(figId)s]

[%(figId)s]: %(url)s "%(title)s" width=%(width)spx\n\n""" % locals()

        return imageLink

    def blockquote(
            self,
            text):
        """*convert plain-text to MMD blockquote*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD blockquote

        **Return:**
            - ``blockquote`` -- the MMD blockquote

        **Usage:**

            To convert a text to a MMD blockquote:

            .. code-block:: python

                text = md.quote(" This is my quote  ")
                print text

                # OUTPUT:
                # >  This is my quote
                #
        """
        m = self.reWS.match(text)
        return "\n> " + ("\n> ").join(m.group(2).split("\n")) + "\n\n"

    def ul(
            self,
            text):
        """*convert plain-text to MMD unordered list*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD unordered list

        **Return:**
            - ``ul`` -- the MMD unordered list

        **Usage:**

            To convert text to a MMD unordered list:

            .. code-block:: python

                ul = md.ul(" This is a list item   ")
                print ul

                # OUTPUT:
                # *  This is a list item
                #
        """
        m = self.reWS.match(text)
        ul = []
        for l in m.group(2).split("\n"):
            prefix, text, suffix = self._snip_whitespace(l)
            ul.append("%(prefix)s* %(text)s  " % locals())

        return ("\n").join(ul) + "\n\n"

    def ol(
            self,
            text):
        """*convert plain-text to MMD ordered list*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD ordered list

        **Return:**
            - ``ol`` -- the MMD ordered list

        **Usage:**

            To convert text to MMD ordered list:

            .. code-block:: python

                ol = md.ol(" This is a list item   ")
                print ol

                # OUTPUT:
                # 1.  This is a list item
                #
        """
        m = self.reWS.match(text)
        ol = []
        for thisIndex, l in enumerate(m.group(2).split("\n")):
            thisIndex += 1
            prefix, text, suffix = self._snip_whitespace(l)
            ol.append("%(prefix)s%(thisIndex)s. %(text)s  " % locals())

        return ("\n").join(ol) + "\n\n"

    def codeblock(
            self,
            text,
            lang=""):
        """*convert plain-text to MMD fenced codeblock*

        **Key Arguments:**
            - ``text`` -- the text to convert to MMD fenced codeblock
            - ``lang`` -- the code language for syntax highlighting. Default *''*

        **Return:**
            - ``text`` -- the MMD fenced codeblock

        **Usage:**

            To convert a text block to comment text:

            .. code-block:: python

                text = md.codeblock("def main()", "python")
                print text

                # OUTPUT:
                # ```python
                # def main()
                # ```
        """
        reRemoveNewline = re.compile(r'^(\s*\n)?([^\n].*?)\s*$', re.S)
        m = reRemoveNewline.match(text)
        text = m.group(2)

        return "\n```%(lang)s\n%(text)s\n```\n" % locals()

    def inline_link(
            self,
            text,
            url):
        """*generate a MMD sytle link*

        **Key Arguments:**
            - ``text`` -- the text to link from
            - ``url`` -- the url to link to

        **Return:**
            - ``text`` -- the linked text

        **Usage:**

            To convert a text and url to MMD link:

            .. code-block:: python

                text = md.inline_link(
                    "  google search engine  ", "  http://www.google.com ")
                print text

                # OUTPUT:
                #   [google search engine](http://www.google.com)
        """
        m = self.reWS.match(text)

        prefix = m.group(1)
        text = m.group(2)
        suffix = m.group(3)
        url = url.strip()

        return "%(prefix)s[%(text)s](%(url)s)%(suffix)s" % locals()

    def _snip_whitespace(
            self,
            text):
        """*snip the whitespace at the start and end of the text*

        **Key Arguments:**
            - ``text`` -- the text to snip

        **Return:**
            - ``prefix``, ``text``, ``suffix`` -- the starting whitespace, text and endding whitespace
        """
        self.log.info('starting the ``_snip_whitespace`` method')

        m = self.reWS.match(text)

        prefix = m.group(1)
        text = m.group(2)
        suffix = m.group(3)

        self.log.info('completed the ``_snip_whitespace`` method')
        return prefix, text, suffix

    def _surround(
            self,
            text,
            left,
            right):
        """*surround text with given characters*

        **Key Arguments:**
            - ``text`` -- the text to surround.
            - ``left`` -- characters to the left of text
            - ``right`` -- characters to the right of text

        **Return:**
            - ``text`` -- the surronded text
        """
        self.log.info('starting the ``_surround`` method')

        prefix, text, suffix = self._snip_whitespace(text)

        text = text.replace("\n\n\n", "\n\n").replace("\n\n\n", "\n\n").replace(
            "\n\n\n", "\n\n").replace("\n\n\n", "\n\n").replace("\n\n", "%(right)s\n\n%(left)s" % locals())

        text = """%(prefix)s%(left)s%(text)s%(right)s%(suffix)s""" % locals()

        self.log.info('completed the ``_surround`` method')
        return text

    # use the tab-trigger below for new method
    # xt-class-method
