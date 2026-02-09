from __future__ import annotations

import shutil
from importlib.resources import files
from pathlib import Path

from cleo.commands.command import Command
from cleo.helpers import argument
from poetry.plugins.application_plugin import ApplicationPlugin

TEMPLATES = files("poetry_hy_plugin") / "templates"


class NewHyCommand(Command):
    name = "new-hy"
    description = "Create a new Hy project"
    arguments = [
        argument("name", "The name of the project"),
    ]

    def handle(self) -> int:
        name = self.argument("name")
        module_name = name.replace("-", "_")
        project_dir = Path(name)

        if project_dir.exists():
            self.line_error(f"<error>Directory '{name}' already exists.</error>")
            return 1

        replacements = {
            "{project_name}": name,
            "{module_name}": module_name,
        }

        # Walk the template tree and copy files with substitutions
        for template_path in TEMPLATES.iterdir():
            _copy_tree(template_path, project_dir, replacements)

        # Rename the placeholder module directory
        placeholder = project_dir / "src" / "hy_project"
        if placeholder.exists():
            placeholder.rename(project_dir / "src" / module_name)

        self.line(f"<info>Created Hy project at</info> <comment>{project_dir}</comment>")
        return 0


def _copy_tree(source, dest_dir, replacements):
    """Recursively copy a template tree, applying text replacements."""
    dest = dest_dir / source.name
    if source.is_dir():
        dest.mkdir(parents=True, exist_ok=True)
        for child in source.iterdir():
            _copy_tree(child, dest, replacements)
    else:
        content = source.read_text()
        for old, new in replacements.items():
            content = content.replace(old, new)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)


class HyPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("new-hy", lambda: NewHyCommand())
