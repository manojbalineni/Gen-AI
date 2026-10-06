import streamlit as slt
slt.title("Streamlit App Demo")
slt.write("This is a demp application created via python and streamlit")

name = slt.text_input("Enter your name")
print(name)


slt.button("Enter" , type = "primary")

slt.date_input("Enter the date of birth")

slt.write("END")
