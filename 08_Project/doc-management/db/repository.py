from db.database import get_connection
from core.models import Document



class DocumentRepository:

  def __init__(self):
    pass


  def save_document(self, doc : Document):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO documents(
        name, path, thumbnail_path, tags, description, upload_date,
        lecture_date, total_pages
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
      ''', 
        (doc.name,
        str(doc.path),
        str(doc.thumbnail_path),
        doc.tags,
        doc.description,
        str(doc.upload_date),
        str(doc.lecture_date) if doc.lecture_date else None,
        doc.total_pages)
      )

    connection.commit()
    connection.close()

  def get_document(self , tag = None, date = None):
    connection = get_connection()
    cursor = connection.cursor()

    query = "Select * from documents"
    conditions = []
    parameters = []

    if tag:
      conditions.append("tags like ?")
      parameters.append(f"%{tag}%")

    if date:
      conditions.append("lecture_date = ?")
      parameters.append(date)


    if conditions:
      last_part = " OR ".join(conditions)
      query += " WHERE " + last_part

    cursor.execute(query , parameters)

    rows = cursor.fetchall()
    connection.close()

    return [Document(*row)  for row in rows]  # List of document objects



  







