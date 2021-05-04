from database_connection import get_database_connection


def drop_tables(connection):
    """Drops the table Notes if it exists

    Args:
        connection ([type]): Connection to the database
    """
    cursor = connection.cursor()

    cursor.execute('''
      drop table if exists Notes
  ''')
    connection.commit()


def create_tables(connection):
    """Creates a table Notes to the database

  Args:
      connection ([type]): Connection to the database
  """
    cursor = connection.cursor()

    cursor.execute("""
      create table Notes(
        id integer primary key autoincrement,
        content text
      )"""
                   )

    connection.commit()


def initialize_database():
    """Connects to the database, then drops Notes table if exists and then creates Notes table.
    """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
