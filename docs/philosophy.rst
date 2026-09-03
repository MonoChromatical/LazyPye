Project philosophy
==================

LazyPye is guided by one goal: provide useful, reusable Python utilities without
making projects depend on unnecessary third-party runtime packages.

Core principles
---------------

* **Standard-library first.** Prefer Python's standard library whenever it can
  provide a clear and maintainable solution.
* **Install only what you need.** Keep broad domains independently installable
  so one utility does not require the entire repository.
* **Keep implementations focused.** Choose understandable behaviour over
  unnecessary abstraction or complexity.
* **Design for growth.** Organize domains into modules and subpackages as their
  real public APIs expand.

Growing the monorepo
--------------------

Create a distribution only when a genuinely separate domain contains real,
usable code. Do not create placeholder distributions in anticipation of possible
future features.

This rule keeps every distribution purposeful while allowing the monorepo to grow
without a fixed package structure.