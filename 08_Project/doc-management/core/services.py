from db.repository import DocumentRepository
from datetime import datetime
import os
from pathlib import Path
from core.file_manager import FileManager
from core.thumbnail import ThumbnailGenerator



BASE_DIR = Path(__file__).resolve().parent.parent
PDF_STORAGE = BASE_DIR / "storage" / "pdfs"



class DocumentService:

  def __init__(self):
    self.document_repository = DocumentRepository()
    self.file_manager = FileManager()
    self.thumbnail_generator = ThumbnailGenerator()


  def upload_documents(self, uploaded_document, tags, description, lecture_date=None):
    file_path = self.file_manager.save_file(uploaded_document)
    print(file_path)
   
    # Generate the thumbnail
    thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)


    # Get the total page count
    total_pages = self.thumbnail_generator.get_total_pages(file_path)
    print(total_pages)
    # Convert images
    # Create intermediate things
    # Save to the DB
    #self.document_repository.save_document(doc) 
  