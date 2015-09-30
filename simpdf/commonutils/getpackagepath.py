#!/usr/local/bin/python
# encoding: utf-8
"""
getpackagepath.py
====================
:Summary:
    Get common file and folder paths for the host package

:Author:
    David Young

:Date Created:
    October 24, 2013

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    - [ ] when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : October 24, 2013
## CREATED : October 24, 2013
## AUTHOR : DRYX

# copy usage method(s) here and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def getpackagepath():
    """getpackagepath

    **Key Arguments:**
        - None

    **Return:**
        - ``packagePath`` -- path to the host package

    **Todo**
        - [ ] when complete, clean worker function and add comments
        - [ ] when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    moduleDirectory = os.path.dirname(__file__)
    packagePath = os.path.dirname(__file__) + "/../"

    return packagePath
###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
