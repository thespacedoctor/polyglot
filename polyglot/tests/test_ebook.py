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
    projectName="polyglot",
    tunnel=False
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

# import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# xt-setup-unit-testing-files-and-folders


class test_ebook():

    def test_epub_function(self):

        from polyglot import ebook
        this = ebook(
            log=log,
            settings=settings,
            urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            title=False,
            bookFormat="epub",
            outputDirectory=pathToOutputDir,
            header=False,
            footer=False
        )
        this._url_to_epub()

        from polyglot import ebook
        epub = ebook(
            log=log,
            settings=settings,
            urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            title=False,
            bookFormat="epub",
            outputDirectory=pathToOutputDir,
            header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
            footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
        )
        pathToEpub = epub.get()
        print pathToEpub

        from polyglot import ebook
        epub = ebook(
            log=log,
            settings=settings,
            urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            title="my first book",
            bookFormat="epub",
            outputDirectory=pathToOutputDir,
            header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
            footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
        )
        pathToEpub = epub.get()
        print pathToEpub

    def test_mobi_function(self):

        from polyglot import ebook
        mobi = ebook(
            log=log,
            settings=settings,
            urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            title=False,
            bookFormat="mobi",
            outputDirectory=pathToOutputDir,
            header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
            footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
        )
        pathToEpub = mobi.get()
        print pathToEpub

        from polyglot import ebook
        mobi = ebook(
            log=log,
            settings=settings,
            urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
            title="my first book",
            bookFormat="mobi",
            outputDirectory=pathToOutputDir,
            header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
            footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
        )
        pathToEpub = mobi.get()
        print pathToEpub

    def test_ebook_function_exception(self):

        from polyglot import ebook
        try:
            this = ebook(
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
