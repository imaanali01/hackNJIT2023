import streamlit as st

st.title("My First Streamlit App")

# Add text input widget
user_input = st.text_input("Enter your name", "Your Name")

# Display a greeting
st.write(f"Hello, {user_input}!")
