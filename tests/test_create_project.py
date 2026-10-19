import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("create_project", ROOT / "scripts" / "create_project.py")
creator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(creator)


class ProjectCreationTests(unittest.TestCase):
    def test_all_templates_copy_full_dependencies_and_record_state(self):
        with tempfile.TemporaryDirectory() as root:
            for template, main in creator.TEMPLATES.items():
                with self.subTest(template=template):
                    project = creator.create_project(template, "测试任务", root, "hybrid", template)
                    task = json.loads((project / "task.json").read_text())
                    self.assertEqual(task["mode"], "hybrid")
                    self.assertEqual(task["template"], template)
                    self.assertEqual(task["main_file"], "report/" + main)
                    self.assertEqual(task["stage"], "intake")
                    for folder in ("materials", "evidence", "work", "deliverables"):
                        self.assertTrue((project / folder).is_dir())
                    self.assertTrue((project / "workflow.md").is_file())
                    source = creator.TEMPLATE_ROOT / template
                    for original in source.rglob("*"):
                        if original.is_file():
                            copied = project / "report" / original.relative_to(source)
                            self.assertEqual(original.read_bytes(), copied.read_bytes())
                    # Report edits must not alter the skill's template.
                    original_main = (source / main).read_bytes()
                    (project / "report" / main).write_text("changed report")
                    self.assertEqual((source / main).read_bytes(), original_main)

    def test_existing_project_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as root:
            project = creator.create_project("experiment", "测试任务", root, name="existing")
            marker = project / "report" / "main.tex"
            marker.write_text("keep my edits")
            with self.assertRaises(FileExistsError):
                creator.create_project("experiment", "另一任务", root, name="existing")
            self.assertEqual(marker.read_text(), "keep my edits")

    def test_unsafe_names_and_skill_destinations_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            for name in ("..", "../escape", "/absolute", "a/b", "a\\b", "", "a\n"):
                with self.subTest(name=name), self.assertRaises(ValueError):
                    creator.create_project("experiment", "测试任务", root, name=name)
            with self.assertRaises(ValueError):
                creator.create_project("experiment", "测试任务", creator.TEMPLATE_ROOT)
            self.assertEqual(list(Path(root).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
