Tutorial
========

Before you begin using polyglot you will need to populate some custom settings within the polyglot settings file.

To setup the default settings file at ``~/.config/polyglot/polyglot.yaml`` run the command:

.. code-block:: bash 
    
    polyglot init

This should create and open the settings file; follow the instructions in the file to populate the missing settings values (usually given an ``XXX`` placeholder). 

polyglot often relies on a bunch on other excellent tools to get it's results like `electron-pdf <https://github.com/fraserxu/electron-pdf>`_, `pandoc <http://pandoc.org>`_ and `kidlegen <https://www.amazon.com/gp/feature.html?docId=1000765211>`_. Depending on how you use polyglot, these tools may need to be install on your system.

To read the basic usage intructions just run ``polyglot -h``.

Webpage Article to HTML document
--------------------------------

To generate a parsed, cleaned local HTML document from a webpage at a given URL use polyglot's ``html`` command:

.. code-block:: bash 
    
    polyglot html https://en.wikipedia.org/wiki/Volkswagen

The filename for the output file is take from the webpage's title and output in the current directory. `Here's the result. <_static/examples/Volkswagen.html>`_
    
To instead give both a destination output and a specified filename for the resulting document:

.. code-block:: bash 
    
    polyglot html https://en.wikipedia.org/wiki/Volkswagen ~/Desktop -f cars_and_stuff

To style the result with polyglots simple styling and easy to read fonts, use the `-c` flag:

.. code-block:: bash 
    
    polyglot -c html https://en.wikipedia.org/wiki/Volkswagen -f Volkswagen_Styled

`See the result here. <_static/examples/Volkswagen_Styled.html>`_

Webpage Article to PDF
----------------------

To instead print the webpage to PDF, you can either just print the original webpage:

.. code-block:: bash 

    polyglot pdf https://en.wikipedia.org/wiki/Volkswagen

`with this result <_static/examples/Volkswagen.pdf>`_, or you can choose again to use polyglot's styling:

.. code-block:: bash 

    polyglot -c pdf https://en.wikipedia.org/wiki/Volkswagen -f Volkswagen_Styled

`resulting in this PDF. <_static/examples/Volkswagen_Styled.pdf>`_

Note if you are going to be running polyglot in a windowless environment, to generate the PDFs with `electron-pdf <`https://github.com/fraserxu/electron-pdf`>`_ you will need to install `xvfb <https://www.x.org/archive/X11R7.6/doc/man/man1/Xvfb.1.xhtml>`_. To install and setup do something similar to the following (depending on your flavour of OS):

.. code-block:: bash 
    
    sudo apt-get install xvfb

then in whatever bash scripts you write add this before any polyglot commands:

.. code-block:: bash
    
    export DISPLAY=':99.0'
    Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &

Webpage Article to eBook
------------------------

To generate an epub book from a webpage article run the command:

.. code-block:: bash 
    
    polyglot epub http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html 

Here is the `output of this command. <_static/examples/mysqlSucker.epub>`_

If you prefer a mobi output, use the command:

.. code-block:: bash 

    polyglot mobi http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html 

To get `this mobi book. <_static/examples/mysqlSucker.mobi>`_

Send a Webpage Article Straight to Your Kindle
----------------------------------------------

Polyglot can go even further than creating a mobi ebook from the web-article; it can also send the ebook straight to your kindle device or smart phone app (or both at the same time) as long as you have the email settings populated in the polyglot settings file.

.. code-block:: bash 
    
    polyglot kindle http://www.thespacedoctor.co.uk/blog/2016/09/26/mysqlSucker-index.html 

And here's the book appearing on a smart phone kindle app:

.. image:: https://i.imgur.com/RQpvBZu.png
    :width: 300 px


