#!/usr/local/bin/python
# encoding: utf-8
"""
*Get common file and folder paths for the host package*

:Author:
    David Young

:Date Created:
    October  4, 2016
"""
import os


def getpackagepath():
    """
     *Get the root path for this python package*

    *Used in unit testing code*
    """
    moduleDirectory = os.path.dirname(__file__)
    packagePath = os.path.dirname(__file__) + "/../"

    return packagePath
