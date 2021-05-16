import unittest
from repositories.note_repository import note_repository


class TestNoteRepository(unittest.TestCase):
    def setUp(self):
        note_repository.delete_all()

        self.note_content = "Muistiinpano"
        self.another_note_content = "Testitapauksia"

    def test_add_note(self):
        note_repository.add_note(self.note_content)
        notes = note_repository.get_all_notes()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0][1], self.note_content)

    def test_get_all_notes(self):
        note_repository.add_note(self.note_content)
        note_repository.add_note(self.another_note_content)
        notes = note_repository.get_all_notes()

        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0][1], self.note_content)
        self.assertEqual(notes[1][1], self.another_note_content)

    def test_delete_note_by_id(self):
        note_repository.add_note(self.note_content)
        note_repository.add_note(self.another_note_content)
        note_repository.delete_all()
        notes = note_repository.get_all_notes()
        self.assertEqual(len(notes), 0)
