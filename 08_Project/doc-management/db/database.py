import os
import sqlite3

DB_PATH = os.path.join("data" , "documents.db")


def get_connection():
  return sqlite3.connect(DB_PATH)


def init_db():
  connection = get_connection()
  cursor = connection.cursor()
  cursor.execute('''
    create table if not exists documents(
    id integer primary key autoincrement,
    name text,
    path text,
    thumbnail_path text,
    tags text,
    description text,
    upload_date text,
    lecture_date text,
    total_pages integer
    )
''')

  cursor.execute('''
      create table if not exists page_visits(
          id integer primary key autoincrement,
          document_id integer,
          page_number integer,
          timestamp text
      )
''')

  connection.commit()
  connection.close()



