import os
import nose
import shutil
import yaml
from polyglot import htmlCleaner, cl_utils
from polyglot.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="polyglot"
)
arguments, settings, log, dbConn = su.setup()

# # load settings
# stream = file(
#     "/Users/Dave/.config/polyglot/polyglot.yaml", 'r')
# settings = yaml.load(stream)
# stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# load settings
stream = file(
    pathToInputDir + "/example_settings.yaml", 'r')
settings = yaml.load(stream)
stream.close()

import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)


# xt-setup-unit-testing-files-and-folders


class test_htmlCleaner():

    def test_htmlCleaner_function(self):

        from polyglot import htmlCleaner
        this = htmlCleaner(
            log=log,
            settings=settings,
            url="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            outputDirectory=pathToOutputDir,
            title=False
        )
        this.clean()

        from polyglot import htmlCleaner
        cleaner = htmlCleaner(
            log=log,
            settings=settings,
            url="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            outputDirectory=pathToOutputDir,
            title="my_clean_doc.html"
        )
        cleaner.clean()

    def test_htmlCleaner_function_exception(self):

        from polyglot import htmlCleaner
        try:
            this = htmlCleaner(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            this.get()
            assert False
        except Exception, e:
            assert True
            print str(e)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
