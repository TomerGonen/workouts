import streamlit as st

st.title("📱 Hello Button App")

if "message" not in st.session_state:
    st.session_state.message = ""

if st.button("Say Hello"):
    st.session_state.message = "hello"

st.text_input("Message:", value=st.session_state.message)
