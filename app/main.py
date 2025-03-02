# app/main.py
import streamlit as st
from app.summarizer import generate_summary
from pdf_parser import parse_pdf

st.set_page_config(page_title="AI-Powered Note Summarizer", layout="wide")

st.title("AI-Powered Note Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
summary_type = st.selectbox("Choose Summary Type", ["Brief", "Detailed", "Technical"])
model = st.selectbox("Choose Model", ["gpt-3.5-turbo", "gpt-4"])
max_tokens = st.slider("Max Tokens", min_value=100, max_value=1000, value=300, step=50)
temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

if uploaded_file is not None:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = parse_pdf(uploaded_file)

    if pdf_text:
        with st.spinner("Generating summary..."):
            summary = generate_summary(pdf_text, summary_type, model, max_tokens, temperature)
            st.subheader("Summary")
            st.write(summary)

            st.download_button("Download Summary as Text File", summary, file_name="summary.txt")
    else:
        st.error("Failed to extract text from the uploaded PDF.")
