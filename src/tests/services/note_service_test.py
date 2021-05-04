import unittest
from services.note_service import NoteService


class FakeNoteRepository:
    def __init__(self, notes=None):
        self.notes = notes or []

    def get_all_notes(self):
        return self.notes

    def add_note(self, content):
        self.notes.append(content)

    def delete_note(self, content):
        self.notes.remove(content)


class TestNoteService(unittest.TestCase):
    def setUp(self):
        self.note_service = NoteService(FakeNoteRepository())
        self.note_content = "First note"
        self.another_note_content = "Second note"

    def test_adding_note(self):
        self.note_service.create_note(self.note_content)
        notes = self.note_service.show_notes()
        self.assertEqual(len(notes), 1)

    def test_showing_added_notes(self):
        self.note_service.create_note(self.note_content)
        self.note_service.create_note(self.another_note_content)
        notes = self.note_service.show_notes()
        self.assertEqual(notes, ["First note", "Second note"])

    def test_delete_notes(self):
        self.note_service.create_note(self.note_content)
        notes = self.note_service.show_notes()
        self.assertEqual(len(notes), 1)
        self.note_service.delete_note_by_id(self.note_content)
        notes = self.note_service.show_notes()
        self.assertEqual(len(notes), 0)
