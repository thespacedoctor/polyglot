#!/usr/local/bin/python
# encoding: utf-8
"""
*Generate a macOS webarchive given the URL to a webpage*

:Author:
    David Young

:Date Created:
    February 24, 2017
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
from fundamentals import tools


class webarchive():
    """
    *Generate a macOS webarchive given the URL to a webpage *

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Usage:**

        To setup your logger, settings and database connections, please use the ``fundamentals`` package (`see tutorial here <http://fundamentals.readthedocs.io/en/latest/#tutorial>`_). 

        Generate a webarchive docuemnt from a URL, use the following:

        .. code-block:: python 

            from polyglot import webarchive
            wa = webarchive(
                log=log,
                settings=settings
            )
            wa.create(url="https://en.wikipedia.org/wiki/Volkswagen",
                      pathToWebarchive=pathToOutputDir + "Volkswagen.webarchive")  
    """

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'webarchive' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def create(self, url, pathToWebarchive):
        """
        *create the webarchive object*

        **Key Arguments:**
            - ``url`` -- the url of the webpage to generate the webarchive for
            - ``pathToWebarchive`` -- tthe path to output the the webarchive file to 

        **Return:**
            - ``webarchive`` -- the path to the webarchive (or -1 if the generation fails)

        **Usage:**

            See class docstring for usage
        """
        self.log.info('starting the ``create`` method')

        from subprocess import Popen, PIPE, STDOUT
        webarchiver = self.settings["executables"]["webarchiver"]
        cmd = """%(webarchiver)s -url %(url)s -output "%(pathToWebarchive)s"  """ % locals()
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        self.log.debug('output: %(stdout)s' % locals())

        if len(stderr) == 0:
            webarchive = pathToWebarchive
        else:
            self.log.error(
                "Could not generate the webarchive for this webpage: %(url)s. %(stderr)s " % locals())
            return -1

        self.log.info('completed the ``create`` method')
        return webarchive

    # xt-class-method
