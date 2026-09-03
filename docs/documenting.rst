Writing Sphinx documentation
============================

This guide explains how contributors should document new LazyPye packages,
modules, classes, methods, and functions.

Documentation structure
-----------------------

Learning material and generated reference material have different jobs:

.. code-block:: text

   docs/
   ├── index.rst
   ├── contributing.rst
   ├── documenting.rst
   ├── packages/
   │   ├── index.rst
   │   └── <feature-guide>.rst
   └── api/
       ├── index.rst
       └── <package-reference>.rst

Pages under `docs/packages` teach people how and why to use a feature. Pages
under `docs/api` provide concise signatures generated from Python docstrings.
A complete feature normally updates both.

Step 1: document the Python code
--------------------------------

Add docstrings to every public class, method, and function. LazyPye supports
Google-style sections through Sphinx's Napoleon extension:

.. code-block:: python

   def add_data(self, data):
       """Append a value to the end of the list.

       Args:
           data: Value to store in the new node.

       Returns:
           None.
       """

State what the object does and document its parameters, return value, raised
exceptions, and important behaviour. Complete tutorials belong in package guides.

Step 2: write the feature guide
-------------------------------

Create or update a page under `docs/packages`. Include:

#. The exact module path and copyable imports.
#. What the feature does and when to use it.
#. Supported capabilities.
#. A complete example with expected output.
#. Every public class and important attribute.
#. Every public method and function.
#. Parameters, return behaviour, examples, and edge cases.

Use the singly linked-list guide as the reference structure.

Step 3: use reStructuredText correctly
--------------------------------------

Sphinx pages use reStructuredText (`.rst`).

.. code-block:: rst

   Page title
   ==========

   Main section
   ------------

   Subsection
   ~~~~~~~~~~

Inline code uses two backticks:

.. code-block:: rst

   Import from `lazypye.data_structures`.

Code directives require a blank line and an indented block:

.. code-block:: rst

   .. code-block:: python

      from lazypye.example import Example

Link to another documentation page with `:doc:`:

.. code-block:: rst

   See :doc:`packages/data-structures` for examples.

Step 4: register the guide in navigation
----------------------------------------

Add the page to the nearest `toctree`. A feature guide normally belongs in
`docs/packages/index.rst`:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2

      data-structures
      new-feature

Paths are relative to the file containing the `toctree` and omit `.rst`.

Leave a source-only comment above each `toctree` so future contributors know
where to register pages:

.. code-block:: rst

   .. Add each new package guide to the toctree below.
      Use its path without the .rst extension.

   .. toctree::
      :maxdepth: 2

      data-structures

reStructuredText comments begin with two periods followed by a space.
Continuation lines must remain indented. Comments are visible to contributors
in the source file but do not appear on the generated site.

Step 5: add generated API documentation
---------------------------------------

Add the module to its package page under `docs/api`:

.. code-block:: rst

   New feature
   -----------

   .. automodule:: lazypye.package_name.module_name
      :members:

Sphinx imports the module and turns public signatures and docstrings into a
reference. The module must be importable in the documentation environment.

For a new distribution, update `docs/conf.py` and the documentation workflow so
its source can be imported during local and GitHub builds.

Step 6: update discovery pages
------------------------------

When adding an entire package, update:

* `docs/packages/index.rst` with its package guide;
* `docs/api/index.rst` with its API reference; and
* `docs/index.rst` if the welcome page should advertise it.

A module inside an existing package usually needs no new homepage entry.

Step 7: build with warnings enabled
-----------------------------------

Install documentation tools:

.. code-block:: console

   py -m pip install -r requirements-docs.txt

Build the site:

.. code-block:: console

   py -m sphinx -W --keep-going -b html docs docs/_build/html

The `-W` option treats warnings as failures. Fix every warning.

Step 8: preview the site locally
--------------------------------

.. code-block:: console

   py -m http.server 8000 --directory docs/_build/html

Open `http://localhost:8000` and check navigation, light and dark themes, code
highlighting, links, examples, API signatures, and mobile-width readability.

Common problems
---------------

Page is missing from navigation
   Add it to the appropriate `toctree` and rebuild.

`automodule` cannot import a module
   Make its source available in `docs/conf.py` or install its distribution into
   the documentation environment.

A link reports an unknown document
   Use a relative documentation path, omit `.rst`, and check capitalization.

Old generated pages remain
   Delete `docs/_build` and perform a clean build.

Code is rendered as ordinary text
   Put a blank line after `code-block` and indent the code consistently.

Final documentation check
-------------------------

Confirm the guide is complete, public docstrings match real behaviour, examples
work, navigation is correct, and the strict build finishes without warnings.