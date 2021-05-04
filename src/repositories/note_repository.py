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
        db = self._connection.cursor()
        db.execute("select * from Notes")
        result = db.fetchall()
        return result

    def add_note(self, content):
      """Adds note to the database

      Args:
          content : The content of the note
      """
        db = self._connection.cursor()
        db.execute("insert into Notes (content) values (?)", [content])

    def delete_note(self, id):
      """Deletes note from the database by note id

      Args:
          id : Note identificator
      """
        db = self._connection.cursor()
        db.execute("delete from Notes where id=?", [id])

    def delete_all(self):
      """Deletes all notes from the database table Notes
      """
        db = self._connection.cursor()
        db.execute("delete from Notes")


note_repository = NoteRepository(get_database_connection())
