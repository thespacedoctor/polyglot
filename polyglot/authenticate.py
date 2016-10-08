#!/usr/local/bin/python
# encoding: utf-8
"""
*Authenticate against readability api*

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
from docopt import docopt
from fundamentals import tools, times


class authenticate():

    """
    *Authenticate against readability api*

    The parser api token is to be found in the polyglot settings file (``~/.config/polyglot/polyglot.yaml``). 

    Read more about readability parser `here <https://www.readability.com/developers/api>`_, or to get your readability parser key sign up to readability and `grab the key here <https://www.readability.com/settings/account>`_

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Usage:**

        To setup a readability parser client:

        .. code-block:: python 

            from polyglot import authenticate
            parserClient = authenticate(
                log=log,
                settings=settings
            ).get() 
    """

    def __init__(
            self,
            log,
            settings=False,

    ):
        self.log = log
        log.debug("instansiating a new 'authenticate' object")
        self.settings = settings
        # xt-self-arg-tmpx

        # Initial Actions

        return None

    def get(self):
        """
        *Get the readability parser client*

        **Return:**
            - ``parserClient`` -- the readability parser client
        """
        self.log.info('starting the ``get`` method')

        from readability import ParserClient
        os.environ['READABILITY_PARSER_TOKEN'] = self.settings[
            "readability"]["parser api token"]

        parser_client = ParserClient()

        self.log.info('completed the ``get`` method')
        return parser_client
