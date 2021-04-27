from database_connection import get_database_connection


class NoteRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_notes(self):
        db = self._connection.cursor()
        db.execute("select * from Notes")
        result = db.fetchall()
        return result

    def add_note(self, content):
        db = self._connection.cursor()
        db.execute("insert into Notes (content) values (?)", [content])

    def delete_note(self, id):
        db = self._connection.cursor()
        db.execute("delete from Notes where id=?", [id])


note_repository = NoteRepository(get_database_connection())
