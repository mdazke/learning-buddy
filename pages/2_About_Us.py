import streamlit as st
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About this App")

st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")



# Check if the password is correct.  
if not check_password():  
    st.stop()

st.header("Project Scope")
st.write("Learning Buddy is an innovative AI-driven tool designed to offer ongoing, personalized support to learners, enabling them to effectively apply the knowledge and skills they acquire in training back to their workplaces")
st.header("Objectives")
st.write("The primary goal of Learning Buddy is to bridge the gap between classroom learning and real-world application by providing post-programme, just-in-time, personalized feedback and support, leveraging the capabilities of a Large Language Model (LLM).")
st.header("Data Sources")
st.write("Course Materials")
st.write("Job Aid")
st.header("Features")
st.write("On-Demand Access: Learners can easily query course materials and job aids at their convenience.")
st.write("Personalized Support: Tailored, context-specific responses help learners address challenges and apply skills in real time.")

# Display a local image
# st.image("./image/image.jpg", caption="Your Image Caption", use_column_width=True)
