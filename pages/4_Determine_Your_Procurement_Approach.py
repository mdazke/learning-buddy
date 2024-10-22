import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Determine Your Procurement Approach")

#st.write("This is a Streamlit App that demonstrates how to use the OpenAI API to generate text completions.")

st.write("In-source vs Outsource")
st.write("Always consider if the need can be met in-house before deciding to purchase")
st.write("Evaluate if the purchase is genuinely needed and prudent")
st.write("Estimated Procurement Value (EPV)")
st.write("Maximum permissible figure")
st.write("Calculation: Base + Options + Contingency sum")
st.write("Minimum Opening Period for ITQ/ITT")
st.write("Open ITQ: 7 working days")
st.write("Open ITT (WTO GPA): 25 working days")
st.write("Open ITT (Non WTO GPA): 14 days")
st.write("WTO-GPA Tenders")
st.write("In exceptional circumstances (safety or public interest), minimum period may be reduced to 10 days")
st.write("Requires prior approval from PS, CEO, or delegated officer")
st.write("Key Consideration")
st.write("The complexity of specifications determines the appropriate opening period")

#with st.expander("How to use this App"):
    #st.write("1. Enter your prompt in the text area.")
    #st.write("2. Click the 'Submit' button.")
    #st.write("3. The app will generate a text completion based on your prompt.")
