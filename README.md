<div align="center">

# LazyPye

### Lightweight Python utilities, installed one domain at a time.

**Standard-library first · Selective installation · Built to grow**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MIT License](https://img.shields.io/badge/license-MIT-2F855A)](LICENSE)
[![Lint](https://github.com/MonoChromatical/LazyPye/actions/workflows/lint.yml/badge.svg)](https://github.com/MonoChromatical/LazyPye/actions/workflows/lint.yml)
[![Documentation](https://github.com/MonoChromatical/LazyPye/actions/workflows/docs.yml/badge.svg)](https://github.com/MonoChromatical/LazyPye/actions/workflows/docs.yml)

[Documentation](https://monochromatical.github.io/LazyPye/) ·
[Package guides](https://monochromatical.github.io/LazyPye/packages/) ·
[Contributing](https://monochromatical.github.io/LazyPye/contributing.html)

</div>

---

## Why LazyPye?

LazyPye is a growing collection of reusable Python utilities that fills gaps in
the standard library without introducing unnecessary third-party runtime
dependencies.

- Install only the broad package domain you need.
- Use consistent imports beneath the shared `lazypye` namespace.
- Rely on focused, understandable implementations.
- Find complete examples and API details in the hosted documentation.

## Installation

Choose a package from the
[package guides](https://monochromatical.github.io/LazyPye/packages/), then replace
`PACKAGE_DIRECTORY` in the Git installation blueprint:

```bash
py -m pip install "git+https://github.com/MonoChromatical/LazyPye.git#subdirectory=packages/PACKAGE_DIRECTORY"
```

When a distribution is published to a Python package index, use its documented
distribution name:

```bash
py -m pip install DISTRIBUTION_NAME
```

Package guides provide the exact installation name, repository directory,
import path, examples, and supported API.

## Documentation

The [LazyPye documentation](https://monochromatical.github.io/LazyPye/) contains:

- Getting-started and installation guidance
- Package-specific tutorials and examples
- Concise generated API references
- Contribution guidelines
- A step-by-step Sphinx documentation guide

Documentation source is maintained in [`docs/`](docs/).

## Contributing

Issues and pull requests are welcome. Read the
[contribution guide](https://monochromatical.github.io/LazyPye/contributing.html)
before implementing a feature, and follow the
[Sphinx documentation guide](https://monochromatical.github.io/LazyPye/documenting.html)
when adding or changing public APIs.

## Status

LazyPye is under active development. Public APIs may evolve as the project
matures.

## License

LazyPye is available under the [MIT License](LICENSE).
