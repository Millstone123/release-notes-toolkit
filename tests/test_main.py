import unittest

from release_notes import render_notes


class ReleaseNotesTests(unittest.TestCase):
    def test_render_notes_groups_changes(self):
        result = render_notes(({"tag": "feature", "summary": "Add CSV export"},))
        self.assertEqual(result, "### Features\n- Add CSV export\n")

    def test_render_notes_handles_all_sections_and_deduplicates(self):
        entries = (
            {"tag": "fix", "summary": "Repair date parsing"},
            {"tag": "feature", "summary": "Add CSV export"},
            {"tag": "other", "summary": "Refresh docs"},
            {"tag": "fix", "summary": "Repair date parsing"},
            {"tag": "other", "summary": ""},
        )
        self.assertEqual(
            render_notes(entries),
            "### Features\n- Add CSV export\n"
            "### Fixes\n- Repair date parsing\n"
            "### Other\n- Refresh docs\n",
        )

    def test_render_notes_preserves_unknown_tags_in_other(self):
        result = render_notes(({"tag": "maintenance", "summary": "Update metadata"},))
        self.assertEqual(result, "### Other\n- Update metadata\n")


if __name__ == "__main__":
    unittest.main()
