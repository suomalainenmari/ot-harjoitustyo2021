from repositories.note_repository import note_repository as default_note_repository


class NoteService:
    def __init__(self, note_repository=default_note_repository):
        self._note_repository = note_repository

    def create_note(self, content):
        return self._note_repository.add_note(content)

    def show_notes(self):
        return self._note_repository.get_all_notes()

    def delete_note_by_id(self, id):
        return self._note_repository.delete_note(id)


note_service = NoteService()
