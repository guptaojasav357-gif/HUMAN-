import streamlit as st
#title of app
st.title("my first streamlit app")
#adding text
st.write("hello! creating a simple web application using streamlit library.")

#text output
name=st.text_input("Enter you name:")
#number input
age=st.number_input("Enter your age:")

#display a message when button is clicked
if st.button("submit"):
  st.write("hello,{name}!welcome to streamlit.")
