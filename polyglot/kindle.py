#!/usr/local/bin/python
# encoding: utf-8
"""
*Send documents or webpage articles to a kindle device or app*

:Author:
    David Young

:Date Created:
    October 10, 2016
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
from fundamentals import tools
from .ebook import ebook
import shutil
import getpass
import optparse
import os
import smtplib
import sys
import traceback
from StringIO import StringIO
from email import encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.generator import Generator


class kindle(ebook):
    """
    *Send documents or webpage articles to a kindle device or app*

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary
        - ``urlOrPath`` -- the url or path to the content source
        - ``title`` -- the title of the output document. I. False then use the title of the original source. Default *False*
        - ``header`` -- content to add before the article/book content in the resulting ebook. Default *False*
        - ``footer`` -- content to add at the end of the article/book content in the resulting ebook. Default *False*

    **Usage:**

        To send content from a webpage article straight to your kindle device or smart phone app, you will first need to populate the email settings with polyglot's settings file at ``~.config/polyglot/polyglot.yaml``, then use the following code:

        .. code-block:: python 

            from polyglot import kindle
            sender = kindle(
                log=log,
                settings=settings,
                urlOrPath="http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html",
                header='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>',
                footer='<a href="http://www.thespacedoctor.co.uk">thespacedoctor</a>'
            )
            success = sender.send()

        Success is True or False depending on the success/failure of sending the email to the kindle email address(es).
    """
    # Initialisation

    def __init__(
            self,
            log,
            settings,
            urlOrPath,
            title=False,
            header=False,
            footer=False
    ):
        self.log = log
        log.debug("instansiating a new 'ebook' object")
        self.settings = settings
        self.title = title
        self.header = header
        self.footer = footer
        self.urlOrPath = urlOrPath
        self.outputDirectory = "/tmp"
        self.format = "mobi"

        # Initial Actions

        return None

    def send(
            self):
        """*send the mobi book generated to kindle email address(es)*

        **Return:**
            - ``success`` -- True or False depending on the success/failure of sending the email to the kindle email address(es).
        """
        self.log.info('starting the ``send`` method')

        pathToMobi = self.get()

        # create MIME message

        msg = MIMEMultipart()
        msg['From'] = self.settings["email"]["user_email"]
        msg['To'] = ", ".join(self.settings["email"]["kindle_emails"])
        msg['Subject'] = 'Headjack to Kindle'
        text = 'This email has been automatically sent by headjack'
        msg.attach(MIMEText(text))

        basename = os.path.basename(pathToMobi)
        print "Sending the mobi book `%(pathToMobi)s` to Kindle device(s)" % locals()
        msg.attach(self.get_attachment(pathToMobi))

        # convert MIME message to string
        fp = StringIO()
        gen = Generator(fp, mangle_from_=False)
        gen.flatten(msg)
        msg = fp.getvalue()

        # send email
        try:
            mail_server = smtplib.SMTP_SSL(host=self.settings["email"]["smtp_server"],
                                           port=self.settings["email"]["smtp_port"])
            mail_server.login(self.settings["email"]["smtp_login"], self.settings[
                              "email"]["smtp_password"])
            mail_server.sendmail(self.settings["email"]["user_email"], ", ".join(self.settings[
                                 "email"]["kindle_emails"]), msg)
            mail_server.close()
        except smtplib.SMTPException:
            os.remove(pathToMobi)
            self.log.error(
                'Communication with your SMTP server failed. Maybe wrong connection details? Check exception details and your headjack settings file')
            return False

        os.remove(pathToMobi)

        self.log.info('completed the ``send`` method')
        return True

    def get_attachment(self, file_path):
        '''Get file as MIMEBase message'''

        try:
            file_ = open(file_path, 'rb')
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(file_.read())
            file_.close()
            encoders.encode_base64(attachment)

            attachment.add_header('Content-Disposition', 'attachment',
                                  filename=os.path.basename(file_path))
            return attachment
        except IOError:
            traceback.print_exc()
            message = ('The requested file could not be read. Maybe wrong '
                       'permissions?')
            print >> sys.stderr, message
            sys.exit(6)

    # xt-class-method
