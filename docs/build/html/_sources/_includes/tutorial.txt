Tutorial
========

Before you begin using polygot you will need to populate some custom settings within the polygot settings file.

To setup the default settings file at ``~/.config/polygot/polygot.yaml`` run the command:

.. code-block:: bash 
    
    polygot init

This should create and open the settings file; follow the instruction in the file to populate the missing settings values (usually given an ``XXX`` placeholder). 

To read the basic usage intructions just run ``polygot -h``

Webpage Article to HTML document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To generate a parsed, cleaned local HTML document from a webpage at a given URL use polygot's ``html`` command:

.. code-block:: bash 
    
    polygot html https://en.wikipedia.org/wiki/Volkswagen 

    





