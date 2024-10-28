import json
import streamlit as st
import pandas as pd
import requests
from PyPDF2 import PdfReader  # Library for reading PDF content
from langchain import hub
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.retrievers.self_query.base import SelfQueryRetriever
#from helper_functions.utility import check_password

# Function to fetch PDF content
def fetch_pdf_content(url):
    response = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)
    
    reader = PdfReader("temp.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# Streamlit App Configuration
st.set_page_config(layout="wide", page_title="Learning Buddy")

# Check password
#if not check_password():
#    st.stop()

# Load job aid content
with open('./data/modules-completed.json', 'r') as f:
    job_aid_content = json.load(f)

# Text Chunking
text_splitter = SemanticChunker(OpenAIEmbeddings())

# Store PDF links and chunk them
pdf_links = [
    "https://thinkscience.co.jp/en/downloads/ThinkSCIENCE-How-to-handle-difficult-QandA-moments.pdf",
    "https://mindfulpresenter.com/wp-content/uploads/2016/03/Final-21-Mindful-Tools-For-Managing-Presentation-Nerves.pdf"
]

# Process PDFs into chunks
for pdf_link in pdf_links:
    try:
        pdf_content = fetch_pdf_content(pdf_link)
        docs = text_splitter.create_documents([pdf_content])
        # Store docs in a vector store here (code for storage not shown)
    except Exception as e:
        st.error(f"Error fetching PDF: {e}")

# Creating two columns for main content and LLM query
left_column, right_column = st.columns([2, 1])

# Left Column - Job Aid Content
with left_column:
    st.title(job_aid_content['job_aid']['title'])
    st.write(job_aid_content['job_aid']['introduction'])

    for section in job_aid_content['job_aid']['sections']:
        st.subheader(section['header'])
        for item in section['content']:
            st.write(f"- {item}")

# Right Column - Learning Buddy
with right_column:
    st.header("Learning Buddy")
    
    # User Interaction Options
    interaction_type = st.selectbox(
        "What would you like to do?",
        ["Review Course Content", "Set a Learning Goal", "Get Application Ideas", "Ask for Help"]
    )

    user_input = st.text_area("Please enter your question or goal here:")

    if st.button("Submit"):
        # Handle different interaction types
        if interaction_type == "Review Course Content":
            st.write("Great! Which topic would you like to review?")
            # Provide a list of topics from job_aid_content for the user to choose from
        elif interaction_type == "Set a Learning Goal":
            st.write(f"Excellent! Your goal is: {user_input}. Let's break it down into actionable steps...")
            # Logic to break down the goal into steps
        elif interaction_type == "Get Application Ideas":
            st.write(f"Sure! Here's how you could apply your learning to: {user_input}.")
            # Logic to generate application ideas
        elif interaction_type == "Ask for Help":
            st.write(f"I'm here to help! You mentioned: {user_input}. Let's approach this step-by-step...")
            # Logic to assist the user with their issue

        # Query Rewriting
        rewrite_template = """Provide a better search query for web search engine to answer the given question, end the queries with '**'. Question: {x} Answer:"""
        rewrite_prompt = ChatPromptTemplate.from_template(rewrite_template)
        
        rewriter = rewrite_prompt | ChatOpenAI(temperature=0) | StrOutputParser()

        # Use Self-Query Retriever for retrieval
        retriever = SelfQueryRetriever()  # Implement and customize this based on your data and indexing

        # Generate response
        prompt_template = """Answer the users question based only on the following context:

        <context>
        {context}
        </context>

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(prompt_template)
        model = ChatOpenAI(temperature=0)

        # Construct retrieval chain
        chain = {
            "context": retriever | RunnablePassthrough(),
            "question": RunnablePassthrough()
        } | prompt | model | StrOutputParser()

        # Invoke chain with user input
        response = chain.invoke({"context": retriever.run(user_input), "question": user_input})

        st.write("Response:", response)

# Additional functionality can be added based on user feedback, logging, etc.
