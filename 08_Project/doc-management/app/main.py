import streamlit as slt
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)


from db.database import init_db
from core.services import DocumentService
from core.analytics import AnalyticsService


if "selected_doc" not in slt.session_state:
  slt.session_state.selected_doc = None


if "current_page" not in slt.session_state:
  slt.session_state.current_page = 0


if "search_results" not in slt.session_state:
  slt.session_state.search_results = []

if "reader_mode" not in slt.session_state:
  slt.session_state.reader_mode = False


init_db()
document_service = DocumentService()
analytics_service = AnalyticsService()

slt.set_page_config(
  page_title = "Doc Manager",
  layout = "wide",

)

slt.title("📚 Smart PDF Document Manager")
slt.divider()

tabs = slt.tabs(["Upload" , "Search and View" , "Analytics"])
with tabs[0]:
  slt.header("Upload PDF")

  uploaded_file = slt.file_uploader("Upload PDF" , type = ["PDF"])
  tags = slt.text_input("Tags(Comma Separated)")
  description = slt.text_area("Description")
  lecture_date = slt.date_input("Lecture Date (Optional)" , value = None)

  if slt.button("Upload"):
    if uploaded_file:
      document_service.upload_documents(uploaded_file , tags , description , lecture_date)
      pass
    else:
      slt.error("Please upload the file")


with tabs[1]:
  slt.header("Search and View")

  col1, col2 = slt.columns(2)

  with col1:
    search_tag = slt.text_input("Search by tag")

  with col2:
    date_tag = slt.date_input("Search by date" , value = None)

  if slt.button("Search"):
    slt.session_state.search_results = document_service.search_document(tag = search_tag if search_tag else None
                                     , date = str(date_tag) if date_tag else None)

    results = slt.session_state.search_results
    if results and not slt.session_state.reader_mode:
      slt.subheader(f"Results : {len(results)} documents")
      container = slt.container(height = 500)

      with container:
        for doc in results:
          #doc -> obj of Document in models.py
          col1 , col2 = slt.columns([1, 3])


          with col1:
            if doc.thumbnail_path:
              slt.image(doc.thumbnail_path , width = 120)


          with col2:
            slt.write(f"**{doc.name}**")
            slt.write(f"Tags : {doc.tags}")
            slt.write(f"Description : {doc.description}")
            slt.write(f"Lecture Date : {doc.lecture_date}")

            if slt.button("Open" , f"open_{doc.id}"):
              slt.session_state.selected_doc = doc
              slt.session_state.current_page = 0
              slt.session_state.reader_mode = True
              slt.rerun()

    if slt.session_state.reader_mode and slt.session_state.selected_doc:
      slt.write("Reader mode is active")

      doc = slt.session_state.slected_doc

      slt.subheader(f"Reading doc : {doc.name}")

      folder_name = os.path.basename(doc.path).replace(".pdf" , "")
      image_dir = f"storage/pdfs/{folder_name}"
      slt.write(f"Images are in {image_dir} directoty")
      slt.write("Files : " , os.listdir(image_dir) if os.path.exists(image_dir) else "Not Found")


      if not os.path.exists(image_dir):
        slt.error("Images not found. PDF Conversion failed")

      else:
        images = sorted(os.listdir(image_dir))
        total_pages = len(images)
        current_page = slt.session_state.current_page


        col1, col2, col3 = slt.columns([1, 2, 1])

        with col1:
          if(slt.button("Previous") and current_page > 0):
            slt.session_state.current_page  -= 1
            slt.rerun()
          

        with col2:
          img_path = os.path.join(image_dir , images[slt.session_state.current_page])
          slt.image(img_path , width = "stretch")

          slt.write(f"FILE : {doc.name}")
          analytics_service.record_page_visit(doc.id , slt.session_state.current_page)

          unique_pages = analytics_service.get_unique_pages_viewed(doc.id)
          progress = (unique_pages / doc.total_pages) * 100 if doc.total_pages else 0

          slt.progress(progress / 100)

          slt.write(f"Progress : {progress:.2f}% ({unique_pages}/{doc.total_pages})")
          



        with col3:
          if(slt.button("Next") and current_page < total_pages - 1):
            slt.session_state.current_page += 1
            slt.rerun()

      if slt.button("Close Reader"):
        slt.session_state.reader_mode = False
        slt.rerun()
        


      

with tabs[2]:
  slt.write("Logic for file analytics")
  pass