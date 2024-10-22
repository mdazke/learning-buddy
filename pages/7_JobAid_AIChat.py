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
    st.title("Determining Your Procurement Approach")
    st.header("Job Aid for Procurement Decisions")

    st.write("""
    This job aid will help you determine the best procurement approach by guiding you through key questions at each stage. 
    Keep this handy as a reference for making procurement decisions.
    """)

    # Section: Why? Possible Questions to Ask
    st.subheader("Why?")
    st.write("""
    - What is the business need for this procurement?
    - What problem are you trying to solve?
    """)

    # Section: What? Possible Questions to Ask
    st.subheader("What?")
    st.write("""
    - What are your critical and non-critical requirements?
    - What market research have you done?
    - What is the budget?
    """)

    # Section: Who? Possible Questions to Ask
    st.subheader("Who?")
    st.write("""
    - Who (other agencies) has procured similar before?
    - Who (potential suppliers) can provide such a product/service?
    - How many suppliers can provide such a product/service?
    - Are there any in-house resources that you can use?
    """)

    # Section: When? Possible Questions to Ask
    st.subheader("When?")
    st.write("""
    - When do you need the product/service to be delivered?
    """)

    # Section: How? Possible Questions to Ask
    st.subheader("How?")
    st.write("""
    - How would you evaluate/measure if the product or service is of the desired quality?
    """)

    # Section for Notes
    st.subheader("Notes")
    st.write("Space for recording the procurement approach(es) advised for the business user:")

    # Workplace Learning Evaluation section
    st.subheader("Workplace Learning Evaluation")
    st.write("""
    **Performance criteria**: Ability to advise the appropriate procurement approach that maximises open & fair competition.

    **Rating options**: 
    - Competent and confident in completing task
    - Not yet competent and confident in completing task
    """)

    # Space for Supervisor Feedback
    st.write("Space for supervisor feedback:")

    # Reminder Section
    st.subheader("Reminder")
    st.write("""
    Complete the 2-minute Course End Check-In on LEARNDC to successfully complete the Step Up Procurement course.
    Keep the job aid for future reference and use.
    """)

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
