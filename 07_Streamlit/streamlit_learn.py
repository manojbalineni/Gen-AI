import streamlit as st

st.set_page_config(
  page_title = "Streamlit Python demo",
  page_icon = "🚀",
  layout = "centered"
)

st.title("Ultimate Data Science")
st.subheader("Level - 1")
st.write("This is batch number 2 of Ultimate Data Science Bootcamp")

tab1 , tab2 , tab3 = st.tabs(["Home", "Dashboard" , "Settings"])


with tab1:
  st.write("Welcome to Home tab !!!")
  left , center , right = st.columns(3)
  with left:
    st.write("Left Section (HOME)")
    st.button("Left Button" , type = "primary")
  with center:
    st.write("Center Section (HOME)")
    st.button("Center Button" , type = "secondary")
  with right:
    st.write("Right Section (HOME)")
    st.button("Right Button" , type = "tertiary")



with tab2:
  st.write("Welcome to Dashboard tab !!!")

with tab3:
  st.write("Welcome to Settings tab !!!")

st.divider()
st.subheader("Level - 2")


with st.container(border = True , height = 200):
  for i in range(100):
    st.write(f"Hello : {i}")

st.divider()

st.subheader("Level - 3 : Input widgets")

if st.button("Clicke Me") : st.write("Hi from the button")

st.link_button(label = "Streamlit widget Redirect" , url = "https://docs.streamlit.io/develop/api-reference/widgets")


name = st.text_input("Enter input ")
st.write(f"Hello, {name}")


count = 0
if(st.button("Click to Add")):
  count = count + 1
  st.write(f"Count of button is {count}")


user_name = st.text_input("Enter username ")
user_password = st.text_input("Enter Password" , type = "password")


bio = st.text_area("Tell us about yourself" , height = 100)
st.write(bio)

st.divider()


st.subheader("Level - 4")
import datetime

today_date = datetime.date.today()
st.write("Today date ", today_date)

picked_date = st.date_input("Pick the date" , today_date)
st.write("Picked date : " , picked_date)

st.divider()

uploaded_file = st.file_uploader("Choose a file" , type = ["csv" , "txt"])

from io import StringIO


if uploaded_file is not None:
  content = StringIO(uploaded_file.getvalue().decode("utf-8"))
  data = content.read()
  st.write("File contents !!")
  st.code(data , language = "text")
  st.write("File uploaded successfully")
  st.success("File uploaded successfylly !")

st.warning("File loading warning")
st.error("Error in uploading file")


st.divider()

if 'count' not in st.session_state:
  st.session_state.count = 0

if st.button("Increment"):
  st.session_state.count += 1
  st.write(f"Button Count : {st.session_state.count}")


st.divider()

st.title("Title")
st.header("Header")
st.subheader("Sub Header")

st.markdown("This is **bold** text")


st.markdown("<h1 style = 'color : red'> This is custom tag </h1>" , unsafe_allow_html = True)


st.divider()

import numpy as np
import pandas as pd

dataframe = pd.DataFrame(np.random.randn(10, 2) , columns = ['A' , 'B'] )
st.write("Streamlit Dataframe visualisation")
st.dataframe(dataframe)


st.write("Streamlit Barchat visualisation")
st.bar_chart(dataframe)


st.image("C:\\Users\\Manoj\\Downloads\\IMG_1901.jpg" , caption = "Sample Image" , width = 250 )

st.divider()

import time
bar = st.progress(0)
for percent in range(100):
  time.sleep(0.01)
  bar.progress(percent + 1)


st.divider()

st.info("Userful info tip")

st.divider()

text = "1, 2, 3, 4, 5"

st.download_button(
    label="Download CSV",
    data=text,
    file_name="sample.csv",
    mime="text/csv",
)