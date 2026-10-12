import os
import pymupdf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
THUMBNAIL_STORAGE = BASE_DIR / "storage" / "thumbnails"


class ThumbnailGenerator:

  def __init__(self):
    pass


  def generate_thumbnail(self , pdf_path):
    THUMBNAIL_STORAGE.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()  # low resolution image -> Compressed image
    base_name = os.path.basename(pdf_path).replace(".pdf" , ".png")
    thumbnail_path = os.path.join(THUMBNAIL_STORAGE , base_name)
    pix.save(thumbnail_path)
    doc.close()
    return thumbnail_path



  def get_total_pages(self , pdf_path):
    doc = pymupdf.open(pdf_path)
    total = len(doc)
    doc.close()
    return total

