import os
import nose
import shutil
import unittest
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
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# xt-setup-unit-testing-files-and-folders


class test_translate(unittest.TestCase):

    def test_translate_function(self):

        longText = """

Praesent laoreet metus vel felis blandit, non hendrerit tellus posuere. Vivamus euismod lectus in nibh luctus posuere. Cras urna diam, bibendum et venenatis sed, malesuada ultrices urna. Etiam ex leo, molestie vel tristique vel, commodo eget libero. Nam eu eros consectetur, semper urna non, accumsan purus. Curabitur gravida vitae est quis molestie. Nullam ac venenatis felis, et convallis neque. Duis et sodales purus, molestie eleifend metus.

Fusce eu mollis ligula. Maecenas vel magna tempus libero dapibus tincidunt. Quisque ac viverra nibh. Fusce fringilla nisi a maximus sollicitudin. Nam dictum, mi a venenatis malesuada, sem odio eleifend turpis, a varius est ante a velit. In faucibus purus ornare luctus finibus. Vivamus faucibus neque augue. Vestibulum ultricies quam vel lectus dictum, vitae euismod justo gravida. In rhoncus molestie purus.

Donec pretium eleifend diam, vel malesuada velit condimentum id. Sed eu placerat diam, nec finibus sapien. Pellentesque non tortor a felis hendrerit volutpat. Duis ultricies odio id viverra dignissim. Aenean faucibus tincidunt leo, sed tincidunt lacus commodo id. Cras sit amet volutpat felis. Nam eu dictum justo.  """

        medText = """Praesent laoreet metus vel felis blandit, non hendrerit tellus posuere. Vivamus euismod lectus in nibh luctus posuere. Cras urna diam, bibendum et venenatis sed, malesuada ultrices urna.

A second paragraph in this medium-length text
        """

        shortText = """ 
Vestibulum pretium pellentesque.  """

        listText = """ 

one
two
    three
    four
five

  """

        from polyglot.markdown import translate
        md = translate(
            log=log,
            settings=settings
        )

        content = ""

        content += md.header("      This is my header  ", level=3)

        content += md.ul(listText[:]) + '\n\n---\n\n'

        content += md.ol(listText[:]) + '\n'

        content += md.bold(longText[:]) + '\n'
        content += md.bold(medText[:]) + '\n'
        content += md.bold(shortText[:]) + '\n'

        content += md.em(longText[:]) + '\n'
        content += md.em(medText[:]) + '\n'
        content += md.em(shortText[:])
        content += md.glossary("Apple", """Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
Also the makers of really great products.""") + '\n'

        content += md.strike(longText[:]) + '\n'
        content += md.strike(medText[:]) + '\n'
        content += md.strike(shortText[:]) + '\n'

        content += md.cite(
            title="a veRy good podcast",
            author="",
            year=False,
            url="http://www.thespacedoctor.co.uk",
            publisher="This Northern Irish Life",
            mediaKind="podcast",
            linkedText=False)

        content += md.underline(longText[:])
        content += md.footnote(longText[:]) + '\n\n'
        content += md.underline(medText[:]).strip()
        content += md.footnote(medText[:]) + '\n\n'
        content += md.underline(shortText[:])
        content += md.footnote(shortText[:]) + '\n\n'

        content += md.cite(
            title="a veRy good podcast, but not cited in doc",
            author="",
            year=False,
            url="http://www.thespacedoctor.co.uk",
            publisher="This Northern Irish Life",
            mediaKind="podcast",
            linkedText=False,
            nocite=True)

        content += md.hl(longText[:]) + '\n'
        content += md.hl(medText[:]) + '\n'
        content += md.hl(shortText[:]) + '\n'

        content += md.cite(
            title="A very good book",
            author="John Doe",
            year=2015,
            url="http://www.thespacedoctor.co.uk",
            publisher="Beefy Books",
            mediaKind=False,
            linkedText="Doe 2015")

        content += md.code(longText[:]) + '\n'
        content += md.code(medText[:]) + '\n'
        content += md.code(shortText[:]) + '\n'

        content += md.comment(longText[:]) + '\n'
        content += md.comment(medText[:]) + '\n'
        content += md.comment(shortText[:]) + '\n'

        content += md.codeblock(longText[:], "perl") + '\n'
        content += md.codeblock(medText[:], "bash") + '\n'
        content += md.codeblock(shortText[:]) + '\n'

        content += md.blockquote(longText[:]) + '\n'
        content += md.blockquote(medText[:]) + '\n'
        content += md.blockquote(shortText[:]) + '\n'

        content += md.url(" https://www.flickr.com ") + '\n'

        content += md.inline_link(
            "         google search engine  ", "  http://www.google.com ")

        content += md.image(
            "http://www.thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png", "thespacedoctor icon", 400)

        content += md.image(
            "http://www.thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png", "thespacedoctor icon")

        content += md.image(
            "http://www.thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png", width=300)

        content += md.image(
            "http://www.thespacedoctor.co.uk/images/thespacedoctor_icon_white_circle.png") + "\n\n\n"

        content += md.headerLink("      This is my header  ") + "\n\n"
        content += md.headerLink("      This is my header  ",
                                 "a link to the a header somewhere") + "\n\n"

        content += md.definition("Apple", """Pomaceous fruit of plants of the genus Malus in the family Rosaceae.
Also the makers of really great products.""")

        content += "\n\nThis is some inline math "

        content += md.math_inline("{e}^{i\pi }+1=0") + ", nice"
        content += md.math_block("{e}^{i\pi }+1=0") + ", nice"

        import codecs
        writeFile = codecs.open(
            pathToOutputDir + "/markdown-output.md", encoding='utf-8', mode='w')
        writeFile.write(content)
        writeFile.close()

    def test_translate_function_exception(self):

        from polyglot.markdown import translate
        try:
            this = translate(
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
