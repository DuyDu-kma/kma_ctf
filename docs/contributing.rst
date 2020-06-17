Contributing
============

Developing on KMActf
~~~~~~~~~~~~~~~~~~
Developing new code for KMActf is easy and fun! KMActf is organized into components which each serve a distinct purpose.


Core Routes/Controllers
-----------------------
The core routes are identified in blueprints in the main KMActf folder for user facing routes and in the KMActf/admin folder for the admin panel. These core routes are used to display theme content and render the main server response that the user will receive.

API Routes/Controllers
----------------------
The API routes are implemented in the ``KMActf/api`` folder as seperate blueprints for each type of resource used in KMActf. Most behavior that manipulates data should be implemented at the API level and seperated by method and resource level. The most common API methods are ``GET``, ``POST``, ``PATCH``, ``DELETE``.

Models
------
KMActf makes heavy usage of the SQLAlchemy ORM to access database contents. The core KMActf models are defined here. Plugins are however capable of adding their own models.

KMActf makes use of ``alembic`` and ``Flask-Migrate`` to perform database migrations between versions.

Schemas
-------
Schemas provide an abstraction layer on top of the database models for permissioning and filtering of data. Schemas and the API work together to make distinctions about what data to show users and what data a user can edit.

Jinja2
------
Jinja2 is used by the KMActf server to render HTML content with data. In some cases (i.e. JavaScript challenge rendering), Mozilla Nunjucks templates are used as a mostly compatible alternative. Any templates written in Nunjucks must still be compatible with Jinja2.

JavaScript & CSS
----------------
JavaScript & CSS are used to style the front end of KMActf.


Linting
~~~~~~~

Python
------
Python code in KMActf is linted with `flake8` and `black`.

Javascript & CSS
----------------
JavaScript and CSS are linted with `prettier`.

.. Tip::
    The recommendation is to integrate all linters into your editor as your changes will fail to pass if the lint checks fail. See the ``Makefile`` for ``make lint``


Testing
~~~~~~~

Python
------

Python tests are run using ``pytest`` on Travis. To run the test suite you can run `make test`. By default tests run against sqlite but this can be configured by setting the `TESTING_DATABASE_URL` environment variable.

KMActf will support both Python 2 and 3 until Python 2's EOL in 2020.

Tests are run in parallel with ``pytest-xdist`` and each test is run in its own database.


Documentation
~~~~~~~~~~~~~

KMActf's documentation is written using Sphinx and hosted by `Read the Docs <https://readthedocs.org/>`_.

To build the documentation, you should go into the ``docs`` folder and run `make html`. The content output into the `docs/_build` folder will be the resulting hosted output.


Tips & Tricks
~~~~~~~~~~~~~
Typically while developing KMActf, developers use the provided ``serve.py`` script or its ``make serve`` wrapper and access KMActf at ``http://localhost:4000``.

Very often you will need to generate testing data so that you can exercise KMActf's behavior. The included ``populate.py`` script will insert randomized testing data into the KMActf database.

The ``export.py`` script can be used to create a KMActf export on the command line.

The ``import.py`` script can be used to load in a KMActf export on the command line.

If you need to wipe KMActf completely, you should:

* empty the cache. By default it will be stored in the ``.data`` folder if Redis is unavailable
* (optional) remove the contents of the `KMActf/uploads` folder
