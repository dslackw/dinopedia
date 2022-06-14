.. contents:: Table of Contents:


About
-----

Dinopedia is a Python application for Dinosaurs Aficionados.


Requirements
------------

.. code-block:: bash

    Flask==2.1.2
    Flask-RESTful==0.3.9
    Flask-Admin==1.6.0
    MarkupSafe==2.1.1
    Flask-SQLAlchemy==2.5.1
    Pillow==9.1.1
    python-dotenv==0.20.0
    psycopg2==2.9.3
    gunicorn==20.1.0


Getting the code
----------------

The code is hosted at https://gitlab.com/dslackw/dinopedia

Check out the with:

.. code-block:: bash

    $ git clone https://gitlab.com/dslackw/dinopedia.git
    $ cd dinopedia


Usage
-----

First build and start a docker container:

.. code-block:: bash
    
    $ docker-compose -f docker-compose.yml build
    $ docker-compose -f docker-compose.yml up -d

If you need to create a dinopedia database:

.. code-block:: bash

    $ docker-compose exec db /bin/bash
    $ psql -U postgres -d postgres
    $ CREATE DATABASE dinopedia;

and restart the container.


.. role:: bash(code)
   :language: bash

The server listens on http://0.0.0.0:8000.

http://0.0.0.0:8000/admin/ Admin interface.

http://0.0.0.0:8000/dinosaurs Find all the available kinds of dinosaurs.

http://0.0.0.0:8000/dinosaurs/<name> Search for a particular kind and get their images.

http://0.0.0.0:8000/dinosaurs/<name> Like your favourite dinosaurs. (:bash:`POST /dinosaurs/<name>?image1=True&image2=True`)

http://0.0.0.0:8000/dinosaurs/favourites See your favourites dinosaurs.


Development
-----------

Start the application in the development environment:

.. code-block:: bash

    $ flask run --host=0.0.0.0 --port=8000


Test data
-----------

Sample data for development/test.

.. code-block:: bash

    $ python3 test_data.py


Details
-------

The application was developed in a Linux Os environment.

Delivery
--------

:Authors: Dimitris Zlatanidis

:Date: 14/06/2022
:Delivery to: GWI