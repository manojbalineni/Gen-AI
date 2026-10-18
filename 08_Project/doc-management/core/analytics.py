from db.database import get_connection
from datetime import datetime

class AnalyticsService:
  def __init__(self):
    pass


  def record_page_visit(self , document_id , page_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
      insert into page_visits (document_id , page_number , timestamp)
      values (? , ? , ?)
      ''' , 
    (document_id , page_number , datetime.now().isoformat()))

    conn.commit()
    conn.close()


  def get_unique_pages_viewed(self , document_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    select count(distnict page_number)
    from page_visits
    where document_id = ?
      ''' , (document_id))
    result = cursor.fetchone()[0]
    conn.close()
    return result if result else 0

  

