from repositories.note_repository import note_repository as default_note_repository


class NoteService:
    """Class for manipulating data in the database
    """

    def __init__(self, note_repository=default_note_repository):
        """Constructor for the class. Creates an object the UI depends on.

        Args:
            note_repository ([type], optional): Performs database queries.
        """
        self._note_repository = note_repository

    def create_note(self, content):
        """Forwards the request for repository-layer for adding a new note

        Args:
            content : The content of the note that is being added

        Returns:
            [type]: [description]
        """
        return self._note_repository.add_note(content)

    def show_notes(self):
        """Forwards the request for repository-layer for fetching all notes

        Returns:
            [type]: [description]
        """
        results = self._note_repository.get_all_notes()
        notes_content = []
        for result in results:
            notes_content.append(result[1])
        return notes_content

    def delete_notes(self):
        """Forwards the request for repository-layer for deleting all notes in database


        Returns:
            [type]: [description]
        """
        return self._note_repository.delete_all()


note_service = NoteService()
