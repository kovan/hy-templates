# hy-templates

Project templates for bootstrapping [Hy](https://hylang.org/) (a Lisp embedded in Python) projects.

All templates generate the same project structure with:
- `src/` layout with `.hy` source files
- `pyproject.toml` with Hy as build + runtime dependency
- `*.hy` package-data configuration (so `.hy` files get included in wheels)
- `conftest.py` for pytest discovery of `.hy` test files
- MIT license

## Templates

### cookiecutter-hy

Universal template using [Cookiecutter](https://github.com/cookiecutter/cookiecutter). Works with any workflow.

```bash
pip install cookiecutter
cookiecutter gh:kovan/hy-templates --directory=cookiecutter-hy
```

Also works with PDM's cookiecutter integration:

```bash
pdm init --cookiecutter https://github.com/kovan/hy-templates --directory=cookiecutter-hy
```

### template-hy

Static [PDM](https://pdm-project.org/) project template.

```bash
pdm new https://github.com/kovan/hy-templates/tree/main/template-hy my-project
```

### poetry-hy-plugin

[Poetry](https://python-poetry.org/) plugin that adds a `new-hy` command.

```bash
poetry self add poetry-hy-plugin
poetry new-hy my-project
```

### hatch-hy

[Hatch](https://hatch.pypa.io/) template plugin (experimental — uses undocumented API).

```bash
pipx inject hatch hatch-hy
```

Then add to `~/.config/hatch/config.toml`:

```toml
[template.plugins.hy]
src-layout = true
```

```bash
hatch new my-project
```

## Generated Structure

```
my-project/
├── pyproject.toml
├── README.md
├── LICENSE
├── conftest.py
├── src/
│   └── my_project/
│       ├── __init__.hy
│       └── main.hy
└── tests/
    └── test_main.hy
```

## Getting Started

After generating a project:

```bash
cd my-project
pip install -e .
hy src/my_project/main.hy    # Hello, Hy!
pytest                        # runs .hy tests via conftest.py
```
