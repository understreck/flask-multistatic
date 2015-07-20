flask-multistatic
=================

:Author: Pierre-Yves Chibon <pingou@pingoured.fr>


This project is a simple `flask`_ plugin to add support for overriding static
files.

Dependencies:
-------------
.. _python: http://www.python.org
.. _Flask: http://flask.pocoo.org/

The dependency list is therefore:

- `python`_ (2.5 minimum)
- `flask`_


Usage:
------

In your flask application:

::

  import flask
  from flask_multistatic import MultiStaticFlask

And replace the way you build you flask application from

::

  APP = flask.Flask(__name__)

by

::

  APP = MultiStaticFlask(__name__)

You can then specify multiple folder where static files are located, for
example:

::

    APP.static_folder = [
        os.path.join(APP.root_path, 'static', APP.config['THEME_FOLDER']),
        os.path.join(APP.root_path, 'static', 'default')
    ]

.. note:: The order of the folder is important, the last folder should be the one
        where most files are present, the other folders are where you override
        the static files.
        So in the example above, all the default static files are in
        `/static/default/` and the files specific for one theme are under
        `/static/<theme_name>/`.


Production:
-----------

Note that this is most likely less efficient than having apache serve the static
files itself, but even if you do that you might want to have multiple static
directories and have apache fallback.

In this case, you can use the example.conf file that is shipped as part of this
repository.

The example.conf file has an example configuration that will try to serve a file
from an instance-specific theme directory, and only if the file was not found, fall
back to the application default theme.


License:
--------

This project is licensed GPLv3+.
