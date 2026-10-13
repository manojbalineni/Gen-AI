from db.repository import DocumentRepository
from datetime import datetime
import os
from pathlib import Path
from core.file_manager import FileManager
from core.thumbnail import ThumbnailGenerator
from core.reader import PDFReader
from core.models import Document



BASE_DIR = Path(__file__).resolve().parent.parent
PDF_STORAGE = BASE_DIR / "storage" / "pdfs"



class DocumentService:

  def __init__(self):
    self.document_repository = DocumentRepository()
    self.file_manager = FileManager()
    self.thumbnail_generator = ThumbnailGenerator()
    self.pdf_reader = PDFReader()


  def upload_documents(self, uploaded_document, tags, description, lecture_date=None):
    file_path = self.file_manager.save_file(uploaded_document)
    print(file_path)
   
    # Generate the thumbnail
    thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)


    # Get the total page count
    total_pages = self.thumbnail_generator.get_total_pages(file_path)
    print(total_pages)


    # Convert images
    self.pdf_reader.convert_pdf_to_images(file_path)

    # Create intermediate things

    upload_date = datetime.now().strftime("%Y-%m-%d")

    # Save to the DB
    doc = Document(
      id = None,
      name = uploaded_document.name,
      path = file_path,
      thumbnail_path = thumbnail_path,
      tags = tags,
      description = description,
      upload_date = upload_date,
      lecture_date = lecture_date,
      total_pages = total_pages
    )
    self.document_repository.save_document(doc) 

  def search_document(self, tag = None , date = None):
    self.document_repository.get_document(tag , date)
  