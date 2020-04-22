Deployment
==========

KMActf is a standard WSGI application so most if not all `Flask documentation`_ on deploying a Flask based application should apply. This page will focus on the recommended ways to deploy KMActf.

.. Important::
   Fully managed and maintained KMActf deployments are available at https://ctfd.io.

Docker
------

KMActf provides automatically generated `Docker images`_ and one of the simplest means of deploying a KMActf instance is to use Docker Compose.

.. Caution:: While Docker can be a very simple means of deploying KMActf, it can make debugging and receiving support more complicated. Before deploying using Docker, be sure you have a cursory understanding of how Docker works.

1. Install `Docker`_
2. Install `Docker Compose`_
3. Clone the KMActf repository with ``git clone https://github.com/KMActf/KMActf.git``
4. Modify the ``docker-compose.yml`` file from the repository to specify a ``SECRET_KEY`` environment for the KMActf service. ::

    environment:
      - SECRET_KEY=<SPECIFY_RANDOM_VALUE>
      - UPLOAD_FOLDER=/var/uploads
      - LOG_FOLDER=/var/log/KMActf
      - DATABASE_URL=mysql+pymysql://root:ctfd@db/ctfd
      - REDIS_URL=redis://cache:6379
      - WORKERS=4

.. Tip::
    You can also run ``python -c "import os; f=open('.ctfd_secret_key', 'a+'); f.write(os.urandom(64)); f.close()"`` within the KMActf repo to generate a .ctfd_secret_key file.

5. Run ``docker-compose up``
6. You should now be able to access KMActf at http://localhost:8000

.. Note::
    The default Docker Compose configuration files do not provide a reverse proxy server or configure SSL/TLS. This is left as an exercise to the reader by design.

Standard WSGI Deployment
------------------------

As a web application, KMActf has a few dependencies which require installation.

1. WSGI server
2. Database server
3. Caching server

WSGI Server
~~~~~~~~~~~

While KMActf is a standard WSGI application and most WSGI servers (e.g. gunicorn, UWSGI, waitress) will likely suffice, KMActf is most commonly deployed with gunicorn. This is because of its simplicity and reasonable performance. It is installed by default and used by other deployment methods discussed on this page. By default it is configured to use gevent as a worker class.


Database Server
~~~~~~~~~~~~~~~

KMActf makes use of SQLAlchemy and as such supports a number of SQL databases. As of KMActf 2.0, the recommended database type is MySQL. KMActf is tested and has been installed against SQLite, Postgres, and MariaDB but this could change in the future.

By default KMActf will create a SQLite database if no database server has been configured.

.. Note::
    KMActf makes use of the JSON data type. MySQL >= 5.7.8 implements a proper JSON type while MariaDB does not. Small differences like these could eventually result in KMActf only supporting a few database servers.

Caching Server
~~~~~~~~~~~~~~

KMActf makes heavy use of caching servers to store configuration values, user sessions, and page content. It is important to deploy KMActf with a caching server. The preferred caching server option is Redis.

By default if no cache server is configured,  KMActf will attempt to use the filesystem as a cache and store values in the ``.data`` folder. This type of caching is not very performant thus it is highly recommended that you configure a Redis server.

Vagrant
-------

KMActf provides a basic Vagrantfile for use with Vagrant. To run using Vagrant run the following commands:

::

    vagrant up

Visit http://localhost:8000 where KMActf will be running.

To access the internal gunicorn terminal session inside Vagrant run:

::

    vagrant ssh
    tmux attach ctfd

.. Note::

    KMActf's Vagrantfile is not commonly used and is only community supported

Debug Server
------------

The absolute simplest way to deploy KMActf merely involves running `python serve.py` to start Flask's built-in debugging server. This isn't recommended for anything but debugging and should not be used for any kind of load. It is discussed here because the debugging server can make identifying bugs and misconfigurations easier. In addition, development mostly occurs using the debug server.

.. Important::
   KMActf makes every effort to be an easy to setup application.
   However, deploying KMActf for large amounts of users can be difficult.

   Fully managed and maintained KMActf deployments are available at https://ctfd.io. If you're interested in a specialized KMActf deployment with custom features please `contact us <https://ctfd.io/contact/>`_.


.. _Flask documentation: http://flask.pocoo.org/docs/latest/deploying/
.. _Docker images: https://hub.docker.com/r/ctfd/ctfd/
.. _Docker: https://docs.docker.com/install/
.. _Docker Compose: https://docs.docker.com/compose/install/
.. _contact us: https://ctfd.io/contact/
