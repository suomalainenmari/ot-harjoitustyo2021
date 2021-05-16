from database_connection import get_database_connection


class NoteRepository:
    """Class where data is stored
    """

    def __init__(self, connection):
        """Constructor for the class. Creates object that performs queries for the database.

        Args:
            connection : Connects to the database
        """
        self._connection = connection

    def get_all_notes(self):
        """Fetches all notes from the database

        Returns:
            [type]: [description]
        """
        notes_db = self._connection.cursor()
        notes_db.execute("select * from Notes")
        result = notes_db.fetchall()
        return result

    def add_note(self, content):
        """Adds note to the database

        Args:
            content : The content of the note
        """
        notes_db = self._connection.cursor()
        notes_db.execute("insert into Notes (content) values (?)", [content])

    def delete_all(self):
        """Deletes all notes from the database table Notes
        """
        notes_db = self._connection.cursor()
        notes_db.execute("delete from Notes")


note_repository = NoteRepository(get_database_connection())
