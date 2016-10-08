import os
import nose
import shutil
import yaml

from polyglot.utKit import utKit

# load settings
stream = file("/Users/Dave/.config/polyglot/polyglot.yaml", 'r')
settings = yaml.load(stream)
stream.close()


# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module

# import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)


class test_printpdf():

    def test_printpdf_function(self):

        from polyglot import printpdf
        pdf = printpdf(
            log=log,
            settings=settings,
            url="https://en.wikipedia.org/wiki/Volkswagen",
            folderpath=pathToOutputDir,
            title=False,
            append=False,
            readability=True
        ).get()

    def test_printpdf_original_function(self):

        from polyglot import printpdf
        pdf = printpdf(
            log=log,
            settings=settings,
            url="https://en.wikipedia.org/wiki/Volkswagen",
            folderpath=pathToOutputDir,
            title=False,
            append="_original",
            readability=False
        ).get()

    def test_printpdf_original_rename_function(self):

        from polyglot import printpdf
        pdf = printpdf(
            log=log,
            settings=settings,
            url="https://en.wikipedia.org/wiki/Volkswagen",
            folderpath=pathToOutputDir,
            title="Cars",
            append="_original",
            readability=False
        ).get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
