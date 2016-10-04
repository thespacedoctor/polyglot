#!/usr/local/bin/python
# encoding: utf-8
"""
*Authenticate against readability api*

:Author:
    David Young

:Date Created:
    September 28, 2015

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times

###################################################################
# CLASSES                                                         #
###################################################################


class authenticate():

    """
    *The worker class for the authenticate module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary


    .. todo::

        - @review: when complete, clean authenticate class
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

    ):
        self.log = log
        log.debug("instansiating a new 'authenticate' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the authenticate object*

        **Return:**
            - ``authenticate``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        from readability import ParserClient
        os.environ['READABILITY_PARSER_TOKEN'] = self.settings[
            "readability"]["parser api token"]

        parser_client = ParserClient()

        self.log.info('completed the ``get`` method')
        return parser_client
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
