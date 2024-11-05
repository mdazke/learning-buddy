import streamlit as st
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App Methodology"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About the Methodology")

st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Display a local image
st.image("./image/workflow.png", caption="Workflow", use_column_width=True)

st.header("Implementation Details")

# Step 1: Define Content Structure
st.header("Step 1: Define Content Structure")
st.write("1. **Learning Content Storage:**")
st.write("• Store your content (e.g., PDFs, text files, videos) in a structured format using JSON.")
st.write("• Ensure each content item is tagged for easy retrieval. Use metadata like topic, level, keywords, and learning objectives.")

# Step 2: Setup the Development Environment
st.header("Step 2: Setup the Development Environment")
st.write("2. **Install Required Libraries:**")
st.write("• First, set up Streamlit and core Python libraries (streamlit, langchain, openai, tiktoken).")
st.write("3. **Prepare Your AI Model (e.g., GPT-4):**")
st.write("• Set up an OpenAI account and retrieve your API key. Use this to integrate GPT-4 or any other LLM.")

# Step 3: Build Core UI in Streamlit
st.header("Step 3: Build Core UI in Streamlit")
st.write("4. **Main UI:**")
st.write("• Create the main interface where users can view course topics and interact with the AI agent.")
st.write("5. **Course Content Page:**")
st.write("• Create content pages with topics and sub-topics, displaying the content effectively.")

# Step 4: Integrate AI in Streamlit
st.header("Step 4: Integrate AI in Streamlit")
st.write("6. **Integrate the AI in Streamlit:**")
st.write("• Use `llm.get_completion_by_messages` function to enable the chat interface in Streamlit.")

# Step 5: Deployment
st.header("Step 5: Deployment")
st.write("7. **Streamlit Cloud Deployment:**")
st.write("• Deploy your Streamlit app using Streamlit Cloud or other platforms like Heroku or AWS.")

