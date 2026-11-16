
import streamlit as st

# Title
st.title("My First Streamlit App")

# User Input
name = st.text_input("Enter your name")

# Display Output
if name:
    st.write("Hello,", name)
