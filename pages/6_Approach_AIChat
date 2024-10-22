import streamlit as st
import pandas as pd
# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",  # Changed layout to "wide" for side-by-side content and LLM query section
    page_title="In-source vs Outsource"
)
# endregion <--------- Streamlit App Configuration --------->

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Creating two columns for main content and LLM query
left_column, right_column = st.columns([2, 1])  # Adjust the column size as needed

# Main content section (left column)
with left_column:
    st.title("In-source vs Outsource")
    st.header("Procurement Decision-Making Guide")

    st.write("""
    Before deciding to outsource or purchase, always consider if the need can be met in-house. 
    Evaluate carefully whether the procurement is necessary and if it is a prudent decision. 
    This guide will walk you through key considerations for making these decisions.
    """)

    # Section: In-source vs Outsource
    st.subheader("In-source vs Outsource")
    st.write("""
    - **In-source:** Always consider if the need can be met in-house before deciding to purchase.
    - **Evaluate:** Ensure the purchase is genuinely needed and prudent.
    """)

    # Section: Estimated Procurement Value (EPV)
    st.subheader("Estimated Procurement Value (EPV)")
    st.write("""
    - **Maximum permissible figure:** Ensure the procurement cost stays within the permissible limit.
    - **Calculation:** Base + Options + Contingency sum.
    """)

    # Section: Minimum Opening Period for ITQ/ITT
    st.subheader("Minimum Opening Period for ITQ/ITT")
    st.write("""
    - **Open ITQ:** 7 working days.
    - **Open ITT (WTO GPA):** 25 working days.
    - **Open ITT (Non-WTO GPA):** 14 days.
    """)

    # Section: WTO-GPA Tenders
    st.subheader("WTO-GPA Tenders")
    st.write("""
    - In exceptional circumstances (e.g., safety or public interest), the minimum period may be reduced to 10 days.
    - Requires prior approval from PS, CEO, or a delegated officer.
    """)

    # Key Consideration section
    st.subheader("Key Consideration")
    st.write("""
    The complexity of specifications will determine the appropriate opening period for the procurement. 
    Carefully assess the level of detail and intricacies of the requirements before setting deadlines.
    """)

# LLM query section (right column)
with right_column:
    st.header("Query the Content")

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
