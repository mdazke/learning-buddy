import json
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",  # Set the layout to 'wide' to enable side-by-side columns
    page_title="Procurement Job Aid"
)
# endregion <--------- Streamlit App Configuration --------->

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Creating two columns for main content and LLM query
left_column, right_column = st.columns([2, 1])  # Adjust the ratio for left and right column sizes

# Main content section (left column)
with left_column:
    # Load the job aid content from the JSON file
    filepath = './data/job-aid.json'
    with open(filepath, 'r') as f:
        job_aid_content = json.load(f)

    # Display the content in Streamlit
    st.title(job_aid_content['job_aid']['title'])
    st.write(job_aid_content['job_aid']['introduction'])

    for section in job_aid_content['job_aid']['sections']:
        st.subheader(section['header'])
        for item in section['content']:
            st.write(f"- {item}")

# LLM query section (right column)
with right_column:
    st.header("Query the Job Aid Content")

    form = st.form(key="query_form")
    form.subheader("Ask a question based on the displayed content")

    user_prompt = form.text_area("Enter your question here", height=200)

    if form.form_submit_button("Submit"):
        st.toast(f"User Input Submitted - {user_prompt}")

        st.divider()

        response, course_details = process_user_message(user_prompt)
        st.write(response)

        st.divider()

        if course_details:
            df = pd.DataFrame(course_details)
            st.dataframe(df)
