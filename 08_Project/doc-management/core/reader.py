import pymupdf
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_STORAGE = BASE_DIR / "storage" / "pdfs"



class PDFReader:
  def __init__(self):
    pass


  def convert_pdf_to_images(self, pdf_path):
    doc = pymupdf.open(pdf_path)
    folder_name = os.path.basename(pdf_path).replace(".pdf", "")
    output_dir = os.path.join(PDF_STORAGE , folder_name)

    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    image_paths = []
    for i in range(len(doc)):
      page = doc.load_page(i)
      matrix = pymupdf.Matrix(2, 2)
      pix = page.get_pixmap(matrix = matrix)
      image_path = os.path.join(output_dir , f"page_{i}.png")
      pix.save(image_path)
      image_paths.append(image_path)

    doc.close()
    return image_paths



