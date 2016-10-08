"""
*Unit testing tools*
"""
from fundamentals import utKit

# OVERRIDES


class utKit(utKit):

    """
    *Override dryx utKit*
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes
    # xdpc-override-utkit-init


# +++++++++++++++++++ NEW CONTENT ++++++++++++++++++


from fundamentals import utKit

# OVERRIDES


class utKit(utKit):

    """
    *Override dryx utKit*
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes
    # Initialisation
    def __init__(
            self,
            moduleDirectory
    ):
        self.moduleDirectory = moduleDirectory
        # x-self-arg-tmpx

        # SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
        self.pathToInputDir = moduleDirectory + "/input/"
        self.pathToOutputDir = moduleDirectory + "/output/"

        # SETUP LOGGING
        self.loggerConfig = """
        version: 1
        formatters:
            file_style:
                format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
                datefmt: '%Y/%m/%d %H:%M:%S'
            console_style:
                format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
                datefmt: '%H:%M:%S'
            html_style:
                format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
                datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
        handlers:
            console:
                class: logging.StreamHandler
                level: DEBUG
                formatter: console_style
                stream: ext://sys.stdout
        root:
            level: DEBUG
            handlers: [console]"""

        # Override Variable Data Atrributes
        self.dbConfig = """
         version: 1
         db: dryx_unit_testing
         host: localhost
         user: unittesting
         password: utpass
         """

        return


# +++++++++++++++++++ NEW CONTENT ++++++++++++++++++


from fundamentals import utKit

# OVERRIDES


class utKit(utKit):

    """
    *Override dryx utKit*
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes
    # Initialisation
    def __init__(
            self,
            moduleDirectory
    ):
        self.moduleDirectory = moduleDirectory
        # x-self-arg-tmpx

        # SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
        self.pathToInputDir = moduleDirectory + "/input/"
        self.pathToOutputDir = moduleDirectory + "/output/"

        # SETUP LOGGING
        self.loggerConfig = """
        version: 1
        formatters:
            file_style:
                format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
                datefmt: '%Y/%m/%d %H:%M:%S'
            console_style:
                format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
                datefmt: '%H:%M:%S'
            html_style:
                format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
                datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
        handlers:
            console:
                class: logging.StreamHandler
                level: DEBUG
                formatter: console_style
                stream: ext://sys.stdout
        root:
            level: DEBUG
            handlers: [console]"""

        # Override Variable Data Atrributes
        self.dbConfig = """
         version: 1
         db: dryx_unit_testing
         host: localhost
         user: unittesting
         password: utpass
         """

        return


# +++++++++++++++++++ NEW CONTENT ++++++++++++++++++


"""
*Unit testing tools*
"""
from fundamentals import utKit

# OVERRIDES


class utKit(utKit):

    """
    *Override dryx utKit*
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes
    # Initialisation
    def __init__(
            self,
            moduleDirectory
    ):
        self.moduleDirectory = moduleDirectory
        # x-self-arg-tmpx

        # SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
        self.pathToInputDir = moduleDirectory + "/input/"
        self.pathToOutputDir = moduleDirectory + "/output/"

        # SETUP LOGGING
        self.loggerConfig = """
        version: 1
        formatters:
            file_style:
                format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
                datefmt: '%Y/%m/%d %H:%M:%S'
            console_style:
                format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
                datefmt: '%H:%M:%S'
            html_style:
                format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
                datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
        handlers:
            console:
                class: logging.StreamHandler
                level: DEBUG
                formatter: console_style
                stream: ext://sys.stdout
        root:
            level: DEBUG
            handlers: [console]"""

        # Override Variable Data Atrributes
        self.dbConfig = """
         version: 1
         db: dryx_unit_testing
         host: localhost
         user: unittesting
         password: utpass
         """

        return
