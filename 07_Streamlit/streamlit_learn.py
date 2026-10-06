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


