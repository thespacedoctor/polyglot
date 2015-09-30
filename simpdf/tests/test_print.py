import os
import nose
import shutil
import yaml
from simpdf import printpdf
from simpdf.utKit import utKit

# load settings
stream = file("/Users/Dave/.config/simpdf/simpdf.yaml", 'r')
settings = yaml.load(stream)
stream.close()


# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_printpdf():

    def test_printpdf_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["settings"] = settings
        kwargs["url"] = "https://en.wikipedia.org/wiki/Volkswagen"
        kwargs["folderpath"] = "/Users/Dave/Desktop"
        # xt-kwarg_key_and_value
        testObject = printpdf(**kwargs)
        testObject.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
