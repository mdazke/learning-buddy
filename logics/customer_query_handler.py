import os
import json
import openai
from helper_functions import llm

category_n_course_name = {'Programming and Development': ['Web Development Bootcamp',
                                                          'Introduction to Cloud Computing',
                                                          'Advanced Web Development',
                                                          'Cloud Architecture Design'],
                          'Data Science & AI': ['Data Science with Python',
                                                'AI and Machine Learning for Beginners',
                                                'Machine Learning with R',
                                                'Deep Learning with TensorFlow'],
                          'Marketing': ['Digital Marketing Masterclass',
                                        'Social Media Marketing Strategy'],
                          'Cybersecurity': ['Cybersecurity Fundamentals',
                                            'Ethical Hacking for Beginners'],
                          'Business and Management': ['Project Management Professional (PMP)Â® Certification Prep',
                                                      'Agile Project Management'],
                          'Writing and Literature': ['Creative Writing Workshop',
                                                     'Advanced Creative Writing'],
                          'Design': ['Graphic Design Essentials', 'UI/UX Design Fundamentals']}

questions_dict = {
    'Why': [
        'What is the business need for this procurement?',
        'What problem are you trying to solve?'
    ],
    'What': [
        'What are your critical and non-critical requirements?',
        'What market research have you done?',
        'What is the budget?'
    ],
    'Who': [
        'Who (other agencies) has procured similar before?',
        'Who (potential suppliers) can provide such a product/service?',
        'How many suppliers can provide such a product/service?',
        'Are there any in-house resources that you can use?'
    ],
    'When': [
        'When do you need the product/service to be delivered?'
    ],
    'How': [
        'How would you evaluate/measure if the product or service is of the desired quality?'
    ]
}

course_topics = {
  "Principles of Procurement": [
    "Transparency in Procurement",
    "Open and Fair Competition",
    "Value for Money in Procurement"
  ],
  "Applying Design Thinking to AOR": [
    "Using Design Thinking Tools for Procurement",
    "Supporting End Users with Empathic Solutions",
    "Design Thinking Principles: Human Centric, Creative and Playful, Iterative, Collaborative, Prototype Driven"
  ],
  "Evaluation and Award": [
    "Evaluation Process: Definition and Importance, Distinct Officer Roles",
    "Bid Corrections: Highlighting Corrections and Recommendations, Handling Disagreements with QAA/TAA"
  ],
  "Strategising a Procurement": [
    "Budget Planning",
    "Solution Consideration",
    "Market Research for EPV",
    "Specification and Evaluation Criteria",
    "Go-To-Market and Proposal Evaluation",
    "Key Concerns in Each Step"
  ],
  "Contract Management": [
    "Delivery Management: Delivery to Contract Specifications, Checking Goods and Services Quality",
    "Relationship Management: Maintaining Open and Constructive Relationships, Managing Issues and Disputes Professionally",
    "Contract Administration: Formal Governance of Contracts, Managing Payment Milestones and Options",
    "Stage 8 Managing Contract Rules: Monitoring Contract Performance, Contracts Variation, Novation, Security Deposit, Handling Poor Performing Contractors, Contract Termination, Contract Review, Debarment of Contractors, Curtailment of Contracts, Bonus Scheme for Construction Quality (BSCQ), Managing Contracts with SOR and Star Rate Items"
  ],
  "Contracts Variation": [
    "Definition and Types of Contract Variations",
    "Minor vs. Substantial Scope Changes",
    "Formal Execution of Contract Variations",
    "Role of Approving Authorities",
    "Good Practice Guide for Approving Variations"
  ]
}


# Load the JSON file
filepath = './data/courses-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

# Load the job aid content from the JSON file
filepath = './data/job-aid.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    job_aid_content = json.loads(json_string)

def identify_category_and_courses(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to any specific courses
    in the Python dictionary below, which each key is a `category`
    and the value is a list of `course_name`.

    If there are any relevant course(s) found, output the pair(s) of a) `course_name` the relevant courses and b) the associated `category` into a
    list of dictionary object, where each item in the list is a relevant course
    and each course is a dictionary that contains two keys:
    1) category
    2) course_name

    {category_n_course_name}

    If are no relevant courses are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    category_and_product_response_str = llm.get_completion_by_messages(messages)
    category_and_product_response_str = category_and_product_response_str.replace("'", "\"")
    category_and_product_response = json.loads(category_and_product_response_str)
    return category_and_product_response

def identify_questions(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with user queries. \
    The user query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to any specific questions
    in the Python dictionary below, which each key is a `category`
    and the value is a list of `question_name`.

    If there are any relevant question(s) found, output the pair(s) of a) `question_name` the relevant question and b) the associated `category` into a
    list of dictionary object, where each item in the list is a relevant question
    and each question is a dictionary that contains two keys:
    1) category
    2) question_name

    {questions_dict}

    If are no relevant questions are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    questions_response_str = llm.get_completion_by_messages(messages)
    questions_response_str = questions_response_str.replace("'", "\"")
    questions_response = json.loads(questions_response_str)
    return questions_response    

def get_course_details(list_of_relevant_category_n_course: list[dict]):
    course_names_list = []
    for x in list_of_relevant_category_n_course:
        course_names_list.append(x.get('course_name')) # x["course_name"]

    print("course_detail_fn : ", course_names_list)

    list_of_course_details = []
    for course_name in course_names_list:
        list_of_course_details.append(dict_of_courses.get(course_name))
    return list_of_course_details

def get_question_details(list_of_relevant_category_n_question: list[dict]):
    question_names_list = []
    for x in list_of_relevant_category_n_question:
        question_names_list.append(x.get('question_name')) # x["question_name"]

    print("question_detail_fn : ", question_names_list)

    list_of_question_details = []
    for question_name in question_names_list:
        list_of_question_details.append(job_aid_content.get(question_name))
    return list_of_question_details

def generate_response_based_on_course_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about course, \
    understand the relevant course(s) from the following list.
    All available courses shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the course to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the course information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the course.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such rating, pricing, and skills to be learnt.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

def generate_response_based_on_question(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about procurement, \
    understand the relevant question(s) from the following list.
    All available questions shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the question to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the question information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the question.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such how it can be applied back at the workplace.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer


def process_user_message(user_input):
    delimiter = "```"

    # print("json :", job_aid_content)

    # Process 1: If Courses are found, look them up
    category_n_course_name = identify_category_and_courses(user_input)
    print("category_n_course_name : ", category_n_course_name)

    # Process 2: Get the Course Details
    course_details = get_course_details(category_n_course_name)
    print("course_detail : ", course_details)

    # Process 3: Generate Response based on Course Details
    reply = generate_response_based_on_course_details(user_input, course_details)


    return reply, course_details

def process_user_message3(user_input):
    delimiter = "```"

    print("json :", job_aid_content)

    # Process 1: If Questions are found, look them up
    questions_name = identify_questions(user_input)
    print("questions_name : ", questions_name)

    # Process 2: Get the Question Details
    question_details = get_question_details(questions_name)
    print("question_detail : ", question_details)

    # Process 3: Generate Response based on Question
    reply = generate_response_based_on_question(user_input, questions_name)
    print("reply : ", reply)


    return reply, questions_name

def process_user_message2(user_prompt):
    # Example logic to check for certain keywords in the prompt
    section = None
    if "Who" in user_prompt:
        section = "Who?"
    elif "When" in user_prompt:
        section = "When?"
    elif "Why" in user_prompt:
        section = "Why?"
    elif "What" in user_prompt:
        section = "What?"
    elif "How" in user_prompt:
        section = "How?"
    
    # Retrieve the section from the job-aid JSON
    if section:
        for sec in job_aid_content['job_aid']['sections']:
            if sec['header'] == section:
                return sec['content'], None
    return "No relevant information found in the job aid.", None

def process_user_message4(user_prompt):
    
    delimiter = "####"

    system_message = f"""
    You are an assistant helping users break down their problems step-by-step.
    The user message will be enclosed within the delimiter {delimiter}.
    
    Analyze the user's message and guide them through three steps:
    
    Step 1: Break down the problem into smaller, manageable parts.
    Step 2: Identify relevant resources from the provided job aid that could assist.
    Step 3: Suggest applying the resources step-by-step and evaluate the outcomes.
    
    Use the following format:
    Step 1:{delimiter} <Detailed reasoning for Step 1>
    Step 2:{delimiter} <Identify any relevant resources from job-aid>
    Step 3:{delimiter} <Provide actionable advice for applying resources>
    
    Ensure the response follows the given format, with {delimiter} separating each step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_prompt}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

def process_user_message5(user_prompt):
    delimiter = "####"

    # Check for keywords in the user prompt and identify a relevant section
    keywords = ["Who", "When", "Why", "What", "How"]
    relevant_section = None

    for keyword in keywords:
        if keyword in user_prompt:
            for section in job_aid_content['job_aid']['sections']:
                if section['header'] == keyword:
                    print(user_prompt)
                    relevant_section = section['content']
                    break
            if relevant_section:
                break

    # If no relevant section is found, provide a fallback message
    if not relevant_section:
        relevant_section = ["No relevant information found in the job aid."]

    

    system_message = f"""
    You are an assistant helping users break down their problems step-by-step.
    The user message will be enclosed within the delimiter {delimiter}.
    
    Analyze the user's message and guide them through three steps:
    
    Step 1: Break down the problem into smaller, manageable parts.
    Step 2: Identify relevant resources from the provided job aid that could assist.
    Step 3: Suggest applying the resources step-by-step and evaluate the outcomes.
    
    Use the following format:
    Step 1:{delimiter} <Detailed reasoning for Step 1>
    Step 2:{delimiter} <Identify any relevant resources from job-aid>
    Step 3:{delimiter} <Provide actionable advice for applying resources>
    
    Ensure the response follows the given format, with {delimiter} separating each step.
    """

    # Prepare the step-by-step guidance
    step_1 = f"Identify the main challenge in your message and break it into simpler components."
    step_2 = f"Here are some relevant resources from the job aid:\n- " + "\n- ".join(relevant_section)
    step_3 = f"Try applying these resources one by one. Start with the first suggestion, evaluate its effectiveness, and proceed with the next."

    # Format the response
    response = f"""
    Step 1:{delimiter} {step_1}
    Step 2:{delimiter} {step_2}
    Step 3:{delimiter} {step_3}
    """

    return response
