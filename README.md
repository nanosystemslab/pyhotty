# pyhot

[![Release](https://img.shields.io/github/v/release/nanosystemslab/pyhot)](https://img.shields.io/github/v/release/nanosystemslab/pyhot)
[![Build status](https://img.shields.io/github/actions/workflow/status/nanosystemslab/pyhot/main.yml?branch=main)](https://github.com/nanosystemslab/pyhot/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/nanosystemslab/pyhot)](https://img.shields.io/github/commit-activity/m/nanosystemslab/pyhot)
[![License](https://img.shields.io/github/license/nanosystemslab/pyhot)](https://img.shields.io/github/license/nanosystemslab/pyhot)

Library to control Omega PID Tempreture Controller. This Python library provides a comprehensive interface for controlling an OMEGA PID temperature controller via Modbus RTU. It supports setting PID parameters, thermocouple types, operational modes, and more. Ideal for precise temperature regulation in industrial and laboratory settings, it simplifies integration with Python projects, enhancing automation and monitoring capabilities.

- **Github repository**: <https://github.com/nanosystemslab/pyhot/>
- **Documentation** <https://nanosystemslab.github.io/pyhot/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:nanosystemslab/pyhot.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/nanosystemslab/pyhot/settings/secrets/actions/new).
- Create a [new release](https://github.com/nanosystemslab/pyhot/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

## Citation

If you use this project in your research, please cite it using the following BibTeX entry:

```bibtex
@software{pyhot,
  author       = {Nakamura, Matthew},
  title        = {pyhot: Library to control Omega PID Tempreture Controller},
  month        = feb,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v0.0.1},
  doi          = {},
  url          = {}
}
```

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
