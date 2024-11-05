import json
import streamlit as st
import pandas as pd
import random
# from helper_functions import llm
from logics.customer_query_handler import process_user_message
from logics.customer_query_handler import process_user_message3
from helper_functions.utility import check_password  

# Function to generate a "Daily Tip"
def get_daily_tip():
    tips = [
        "Tip: Consistency is key! Dedicate a small amount of time each day to your learning.",
        "Tip: Don't be afraid to ask for feedback from colleagues to improve your skills.",
        "Tip: Apply what you learn in real-world scenarios to make it stick.",
        "Tip: Take regular breaks to keep your mind fresh and focused."
    ]
    daily_tip = random.choice(tips)
    st.write(f"💡 {daily_tip}")

# Initialize session state variables if not already done
if "current_function" not in st.session_state:
    st.session_state.current_function = "Review Course Content"

# Load the JSON file
filepath = './data/course-topics-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

# # Functions for each option
# def review_course_content():
#     st.subheader("Review Course Content")
#     st.write("Provide detailed information to help you review your course content.")

# def set_learning_goal():
#     st.subheader("Set a Learning Goal")
#     st.write("Set clear and achievable goals for your learning journey.")

# def get_application_ideas():
#     st.subheader("Get Application Ideas")
#     st.write("Explore practical ideas to apply your course content effectively.")

# def ask_for_help():
#     st.subheader("Ask for Help")
#     st.write("Describe the help you need to overcome learning obstacles.")


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",  # Set the layout to 'wide' to enable side-by-side columns
    page_title="Learning Buddy"
)
# endregion <--------- Streamlit App Configuration --------->

# Check if the password is correct.  
if not check_password():  
    st.stop()

# Function to handle "Review Course Content"
def review_course_content():
    st.header("📚 Review Course Content")
    st.write("🤖 : Great! Which topic would you like to review?")
    # Display a list of course topics
    course_topics = list(dict_of_courses.keys())
    selected_topic = st.selectbox("Select a course topic", course_topics)
    if selected_topic:
        st.write(f"You selected: {selected_topic}")
        course_details = dict_of_courses.get(selected_topic, "Course details not found.")
        st.write(course_details)

# Function to handle "Set a Learning Goal"
def set_learning_goal():
    st.header("🎯 Set a Learning Goal")
    st.write("🤖 : Excellent! What skill from the course would you like to focus on this week?")
    goal = st.text_input("Enter your learning goal")
    if goal:
        print(f"{goal}")
        st.write(f"That's a great goal: {goal}. Let's break it down into actionable steps...")
        steps = [
            "Step 1: Identify key concepts related to your goal.",
            "Step 2: Dedicate time each day to practice.",
            "Step 3: Reflect on what you've learned and apply it at work."
        ]
        for step in steps:
            st.write(f"- {step}")

# Function to handle "Get Application Ideas"
def get_application_ideas():
    st.header("💡 Get Application Ideas")
    st.write("🤖 : Sure! What's your current task or challenge at work?")
    task = st.text_area("Describe your current task or challenge", height=150)
    if task:
        st.write(f"Based on your course, here are some ways you could apply your learning to '{task}':")
        ideas = [
            "Idea 1: Apply the key concepts to solve your problem.",
            "Idea 2: Use techniques from the course to enhance your work output.",
            "Idea 3: Collaborate with colleagues and share your insights."
        ]
        for idea in ideas:
            st.write(f"- {idea}")

# Function to handle "Ask for Help"
def ask_for_help():
    st.header("🆘 Ask for Help")
    st.write("Job Aid: Determining Your Procurement Approach")
    form = st.form(key="query_form")
    form.subheader("🤖 : I'm here to help! What are you struggling with?")

    user_prompt = form.text_area("Describe your issue", height=200)

    if form.form_submit_button("Submit"):
       st.toast(f"User Input Submitted - {user_prompt}")

       st.divider()

       response = process_user_message3(user_prompt)
       st.write(response)

    
# Creating two columns for main content and LLM query
left_column, right_column = st.columns([2, 1])  # Adjust the ratio for left and right column sizes

# Main content section (left column)
with left_column:
    # Load the job aid content from the JSON file
    filepath = './data/course-topics.json'
    with open(filepath, 'r') as file:
        course_topics = json.load(file)

    # Load the job aid content from the JSON file
    filepath = './data/job-aid.json'
    with open(filepath, 'r') as f:
        job_aid_content = json.load(f)

    # Display the course topics
    for topic in course_topics["courseTopics"]:
        st.divider()
        st.header(topic["title"])
        for subtopic in topic["subtopics"]:
            if isinstance(subtopic, dict):
                # If subtopic is a dictionary, iterate over its items
                for key, values in subtopic.items():
                    st.subheader(key)
                    for value in values:
                        st.write(f"- {value}")
            else:
                # If subtopic is a string, display it directly
                st.write(f"- {subtopic}")

    st.divider()
    
    # Display the content in Streamlit
    st.title(job_aid_content['job_aid']['title'])
    st.write(job_aid_content['job_aid']['introduction'])

    for section in job_aid_content['job_aid']['sections']:
        st.subheader(section['header'])
        for item in section['content']:
            st.write(f"- {item}")

# LLM query section (right column)
with right_column:
    st.header("Learning Buddy")

    # Display the daily tip
    st.divider()
    st.write("Here's your daily tip:")
    get_daily_tip()

    # if st.button("📚 Review Course Content"):
    #     st.write("Reviewing Course Content...")
    #     review_course_content()

    # if st.button("🎯 Set a Learning Goal"):
    #     st.write("Setting a Learning Goal...")
    #     set_learning_goal()

    # if st.button("💡 Get Application Ideas"):
    #     st.write("Get Application Ideas")
    #     get_application_ideas()

    # if st.button("🆘 Ask for Help"):
    #     ask_for_help()
    #     st.write("Ask for Help")
        ###
        # Creating a form to capture user input without page refresh
        # with st.form(key="query_form"):
        #     st.subheader("I'm here to help! What are you struggling with?")
        #     user_prompt = st.text_area("Describe your issue", height=200)
        #     submit_button = st.form_submit_button("Submit")
        #     print(f"{user_prompt}")

        #     if submit_button:
        #         st.toast(f"User Input Submitted - {user_prompt}")
        #         response = process_user_message3(user_prompt)
        #         st.write(response)
        #         st.divider()
        ###
        # form = st.form(key="query_form")
        # form.subheader("I'm here to help! What are you struggling with?")

        # user_prompt = form.text_area("Describe your issue", height=200)

        # if form.form_submit_button("Submit"):
        #     st.toast(f"User Input Submitted - {user_prompt}")
        # print(f"{user_prompt}")
        # st.divider()

        # response = process_user_message3(user_prompt)
        # st.write(response)

        # st.divider()

    # Sidebar to control which function to show
    options = [
        "Review Course Content",
        "Set a Learning Goal",
        "Get Application Ideas",
        "Ask for Help"
    ]

    st.sidebar.header("🤖 : Choose an Option")
    selected_option = st.sidebar.radio("Select an action:", options)
    st.session_state.current_function = selected_option

    # Display the selected function
    if st.session_state.current_function == "Review Course Content":
        review_course_content()
    elif st.session_state.current_function == "Set a Learning Goal":
        set_learning_goal()
    elif st.session_state.current_function == "Get Application Ideas":
        get_application_ideas()
    elif st.session_state.current_function == "Ask for Help":
        ask_for_help()

    # User input form for asking for help
    st.divider()  # Add a divider between the options and the form

    # form = st.form(key="query_form")
    # form.subheader("I'm here to help! What are you struggling with?")

    # user_prompt = form.text_area("Describe your issue", height=200)

    # if form.form_submit_button("Submit"):
    #    st.toast(f"User Input Submitted - {user_prompt}")

    #    st.divider()

    #    response = process_user_message3(user_prompt)
    #    st.write(response)

    # print("TEST!")
    # print(course_topics)

    #    st.divider()

    #    if course_details:
    #        df = pd.DataFrame(course_details)
    #        st.dataframe(df)
