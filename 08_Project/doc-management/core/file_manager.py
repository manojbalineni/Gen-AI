from datetime import datetime
import os
from pathlib import Path
import traceback


BASE_DIR = Path(__file__).resolve().parent.parent
PDF_STORAGE = BASE_DIR / "storage" / "pdfs"

class FileManager:
  def __init__(self):
    pass


  def save_file(self, uploaded_document):
    try:
        PDF_STORAGE.mkdir(parents=True, exist_ok=True)
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{time_stamp}_{uploaded_document.name}"
        file_path = (PDF_STORAGE / file_name).resolve()
        print("Saving to:", file_path)

        data = uploaded_document.getbuffer()
        print("Bytes to write:", len(data))

        with open(file_path, "wb") as f:
            f.write(data)

        print("Exists after write:", file_path.exists(), file_path.stat().st_size)
        return file_path
    except Exception:
        traceback.print_exc()
        raise
    