# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

# Create an expander
with st.expander("Click to Expand"):
    st.title("IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype.")
    st.write("The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
    st.write("Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
    st.write("Always consult with qualified professionals for accurate and personalized advice.")

# Check if the password is correct.  
if not check_password():  
     st.stop()

st.write("This is a proof-of-concept project for the AI Bootcamp Project.")

# form = st.form(key="form")
# form.subheader("Prompt")

# user_prompt = form.text_area("Enter your prompt here", height=200)

# if form.form_submit_button("Submit"):
    
#     st.toast(f"User Input Submitted - {user_prompt}")

#     st.divider()

#     response, course_details = process_user_message(user_prompt)
#     st.write(response)

#     st.divider()

#     print(course_details)
#     df = pd.DataFrame(course_details)
#     df 
