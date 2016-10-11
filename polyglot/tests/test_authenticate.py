import os
import nose
import shutil
import yaml
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


class test_authenticate():

    def test_authenticate_function(self):

        from polyglot import authenticate
        parserClient = authenticate(
            log=log,
            settings=settings
        ).get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
