import streamlit as slt
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)


from db.database import init_db

init_db()

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
    if not uploaded_file:
      pass

with tabs[1]:
  slt.write("Logic for viewing the file")
  pass

with tabs[2]:
  slt.write("Logic for file analytics")
  pass