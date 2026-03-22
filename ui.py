import streamlit as st
from app import ask_question

st.set_page_config(page_title="RAG Resume Assistant")

st.title("🧠 RAG Resume Assistant")
st.write("Ask questions about your resume")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        answer = ask_question(question)
        st.write("### Answer")
        st.write(answer)