import os
import json
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate


with open("./data/course-files.json", "r") as f:
    pdf_paths = json.load(f)["pdf_files"]

st.title("Course Summarizer with LangChain and FAISS")
st.write("Summarizes all course material in pdf files")

#os.environ["OPENAI_API_KEY"] = "Please key in API key"

pdf_documents = {}

for pdf_path in pdf_paths:
    loader = PyPDFLoader(pdf_path)
    pdf_documents[pdf_path] = loader.load()


llm = ChatOpenAI(model_name="gpt-4o-mini")
summaries = []

st.subheader("Generated Summaries:")

for pdf_path in pdf_paths:
    prompt=ChatPromptTemplate.from_messages(
        [("system", "Write a three point summary of the following:\\n\\n{context}")]
    )
    chain=create_stuff_documents_chain(llm, prompt)
    summary = chain.invoke({"context":pdf_documents[pdf_path]})
    st.markdown(f"### Summary for {pdf_path}:")
    st.write(summary)




