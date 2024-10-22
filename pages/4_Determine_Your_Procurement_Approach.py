import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="In-source vs Outsource"
)
# endregion <--------- Streamlit App Configuration --------->

# Title and header
st.title("In-source vs Outsource")
st.header("Procurement Decision-Making Guide")

# Introduction
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
