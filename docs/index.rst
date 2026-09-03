Welcome to LazyPye
==================

A universal, growing collection of reusable Python utilities that fills gaps in
the standard library without introducing third-party runtime dependencies.

LazyPye is a monorepo of independently installable packages, so users install only
the domain they need.

.. important::

   LazyPye is under active development. APIs may change as the library grows.

Get started
-----------

Choose the domain containing the utility you need from :doc:`packages/index`.
Each package guide provides its exact installation command, imports, and usage
examples.

LazyPye packages follow this reusable Git installation blueprint:

.. code-block:: console

   py -m pip install "git+https://github.com/MonoChromatical/LazyPye.git#subdirectory=packages/PACKAGE_DIRECTORY"

Replace `PACKAGE_DIRECTORY` with the repository directory shown in the selected
package guide. See :doc:`getting-started` for the complete installation process.

Explore LazyPye
---------------

:doc:`getting-started`
   Installation requirements and the reusable package-installation blueprint.

:doc:`packages/index`
   Guides for every available package and feature.

:doc:`api/index`
   Exact public classes, methods, signatures, and docstrings.

:doc:`contributing`
   Coding standards and the complete feature contribution workflow.

Why LazyPye?
------------

* **Standard-library first:** avoid unnecessary runtime dependencies.
* **Reusable:** share focused utilities across many projects.
* **Lightweight:** keep implementations understandable and efficient.
* **Selective:** install only the broad package domain you need.
* **Expandable:** grow into new domains without becoming one large install.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Start here

   getting-started
   philosophy

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Packages

   packages/index

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Reference

   api/index
   contributing
   documenting

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
