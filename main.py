# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
# from logics.customer_query_handler import process_user_message
from helper_functions.utility import check_password  

# Initialize session state if not already done
if "message" not in st.session_state:
    st.session_state.message = "Welcome! Click any button to display a message."

# Functions to update the message for each button
def show_message1():
    st.session_state.message = "This is the first message!"

def show_message2():
    st.session_state.message = "This is the second message!"

def show_message3():
    st.session_state.message = "This is the third message!"


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

with st.expander("How to use this App"):
    st.write("1. Click on Learning Buddy on the left navigation bar.")
    st.write("2. Choose from the four options that Learning Buddyy offers from the left navigation bar.")
    st.write("3. Select either Review Course Content, Get Application Ideas or the Ask for Help option. This is where most of the LLM codes are.") 
    st.write("4. This draws from either the content or Job Aid Questions to further help the query.")
    st.write("5. Ask keywords from the Content(i.e. Contract Variation, Transparency)/ Job Aid (i.e Market Research, Suppliers)")
    st.write("6. Enter your prompt in the text area.")
    st.write("7. Click the 'Submit' button.")
    st.write("8. The app will generate a text completion based on your prompt.")
    st.write("Note: If the app provides a nil return, try to hit submit again or re-select a differnt option. We seek your patience as it's only a prototype.")

# # Display the buttons
# st.button("Show Message 1", on_click=show_message1)
# st.button("Show Message 2", on_click=show_message2)
# st.button("Show Message 3", on_click=show_message3)

# # Display the current message
# st.write(st.session_state.message)

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
