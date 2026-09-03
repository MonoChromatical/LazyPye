Getting started
===============

Requirements
------------

LazyPye requires Python 3.10 or newer. Library packages avoid third-party runtime
dependencies.

Choose a package
----------------

LazyPye distributions are independently installable. Use :doc:`packages/index` to
find the domain containing the feature you need, then use that package's
documented distribution name or repository directory.

Installation blueprint
----------------------

Install a distribution directly from this Git repository with:

.. code-block:: console

   py -m pip install "git+https://github.com/MonoChromatical/LazyPye.git#subdirectory=packages/PACKAGE_DIRECTORY"

Replace `PACKAGE_DIRECTORY` with the folder named by the package guide. Do not
run the blueprint without replacing that value.

When a distribution is published to a Python package index, install it with:

.. code-block:: console

   py -m pip install DISTRIBUTION_NAME

Replace `DISTRIBUTION_NAME` with the exact install name shown in its package
guide. Distribution names used by `pip` can differ from Python import paths.

Installation and imports are separate
-------------------------------------

A distribution may use a hyphenated install name while exposing an underscored
Python import path:

.. code-block:: text

   Install name: lazypye-package-name
   Import path:  lazypye.package_name

Always copy both values from the relevant package guide rather than deriving one
from the other.

Using an installed package
--------------------------

Each page under :doc:`packages/index` provides exact imports, capabilities,
examples, expected output, and edge-case behaviour. The :doc:`api/index` is a
compact lookup for public signatures and docstrings.