#!/usr/local/bin/python
# encoding: utf-8
"""
Documentation for polyglot can be found here: http://pypolyglot.readthedocs.org/en/stable

Translate documents and webpages to various markup languages and document formats (html, epub, mobi ..)

Usage:
    polyglot init
    polyglot [-oc] (pdf|html|epub|mobi) <url> [<destinationFolder> -f <filename> -s <pathToSettingsFile>]
    polyglot kindle <url> [-f <filename> -s <pathToSettingsFile>]

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
    -s <pathToSettingsFile>, --settings <pathToSettingsFile>        path to alternative settings file (optional)
    <destinationFolder>                                             the folder to save the parsed PDF or HTML document to (optional)
    -f <filename>, --filename <filename>                            the name of the file to save, otherwise use webpage title as filename (optional)
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from subprocess import Popen, PIPE, STDOUT
from docopt import docopt
from fundamentals import tools, times
from polyglot import printpdf
from polyglot import htmlCleaner
# from ..__init__ import *


def main(arguments=None):
    """
    *The main function used when ``cl_utils.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=False,
        projectName="polyglot"
    )
    arguments, settings, log, dbConn = su.setup()

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE cl_utils.py AT %s' %
        (startTime,))

    # for k, v in locals().iteritems():
    #     print k, v

    if not destinationFolder:
        destinationFolder = os.getcwd()
    if not filenameFlag:
        filenameFlag = False
    if not cleanFlag:
        readability = False
    else:
        readability = True

    if init:
        from os.path import expanduser
        home = expanduser("~")
        filepath = home + "/.config/polyglot/polyglot.yaml"
        try:
            cmd = """open %(filepath)s""" % locals()
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        except:
            pass
        try:
            cmd = """start %(filepath)s""" % locals()
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        except:
            pass

    if pdf:
        filepath = printpdf.printpdf(
            log=log,
            settings=settings,
            url=url,
            folderpath=destinationFolder,
            title=filenameFlag,
            append=False,
            readability=readability
        ).get()

    if html:

        cleaner = htmlCleaner.htmlCleaner(
            log=log,
            settings=settings,
            url=url,
            outputDirectory=destinationFolder,
            title=filenameFlag,  # SET TO FALSE TO USE WEBPAGE TITLE,
            style=cleanFlag,  # add polyglot's styling to the HTML document
            metadata=True,  # include metadata in generated HTML (e.g. title),
            h1=True  # include title as H1 at the top of the doc
        )
        filepath = cleaner.clean()

    if epub:
        from polyglot import ebook
        epub = ebook(
            log=log,
            settings=settings,
            urlOrPath=url,
            title=filenameFlag,
            bookFormat="epub",
            outputDirectory=destinationFolder
        )
        filepath = epub.get()

    if mobi:
        from polyglot import ebook
        mobi = ebook(
            log=log,
            settings=settings,
            urlOrPath=url,
            title=filenameFlag,
            bookFormat="mobi",
            outputDirectory=destinationFolder,
        )
        filepath = mobi.get()

    if kindle:
        from polyglot import kindle
        sender = kindle(
            log=log,
            settings=settings,
            urlOrPath=url,
            title=filenameFlag
        )
        success = sender.send()

    if openFlag:
        try:
            cmd = """open %(filepath)s""" % locals()
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        except:
            pass
        try:
            cmd = """start %(filepath)s""" % locals()
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        except:
            pass

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


if __name__ == '__main__':
    main()
