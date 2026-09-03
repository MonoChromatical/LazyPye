Contributing
============

Contributions should preserve LazyPye's standard-library-first philosophy, remain
easy to discover, and include complete user-facing documentation.

Before you begin
----------------

* Confirm the feature does not add an unnecessary third-party runtime dependency.
* Choose the existing package domain that best owns the feature.
* Create a new distribution only when real code exists for a separate domain.
* Keep imports beneath the shared `lazypye` namespace.
* Discuss breaking public API changes before implementation.

Feature implementation workflow
-------------------------------

1. Choose the package and module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place the implementation beneath the matching distribution:

.. code-block:: text

   packages/PACKAGE_DIRECTORY/src/lazypye/PACKAGE_NAME/MODULE_NAME.py

Use lowercase `snake_case` module names and descriptive public names.

2. Implement the feature
~~~~~~~~~~~~~~~~~~~~~~~~

Prefer Python's standard library, keep behaviour predictable, handle important
boundary cases, and document every public class, method, and function.

3. Add tests
~~~~~~~~~~~~

Cover normal use, edge cases, expected failures, and examples. A public feature
is not complete until its documented behaviour is tested.

4. Update documentation
~~~~~~~~~~~~~~~~~~~~~~~

Update the relevant package guide and generated API page. The package guide
should teach usage; the API page should provide signatures and docstrings.

Follow :doc:`documenting` for the authoritative feature-guide checklist,
reStructuredText syntax, navigation, API generation, and preview instructions.

5. Run project checks
~~~~~~~~~~~~~~~~~~~~~

Replace `PACKAGE_DIRECTORY` before running the package-install command:

.. code-block:: console

   ruff check .
   pytest
   py -m pip install ./packages/PACKAGE_DIRECTORY
   py -m sphinx -W --keep-going -b html docs docs/_build/html

6. Review the finished change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confirm imports and examples work exactly as documented, generated files are not
included, and the change does not create placeholder package directories.

Submission checklist
--------------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Requirement
     - Complete
   * - Correct package and module location
     - [ ]
   * - Exact installation and import commands
     - [ ]
   * - User guide and public docstrings updated
     - [ ]
   * - Normal, edge, and failure cases tested
     - [ ]
   * - Ruff and pytest pass
     - [ ]
   * - Sphinx builds without warnings
     - [ ]
