from database_connection import get_database_connection

class NoteRepository:
  def __init__(self,connection):
    self._connection = connection

  def get_all_notes(self):
    db = self._connection.cursor()
    db.execute("select * from notes")
    result = db.fetchall()
    return result

  def add_note(self, content):
    db = self._connection.cursor()
    content = content
    db.execute("insert into Notes (content) values (?)", [content])
    forprinting = self.get_all_notes()

  def delete_note(self,id):
    db = self._connection.cursor()
    db.execute("delete from Notes where id=?", [id])
    
  

note_repository = NoteRepository(get_database_connection())
