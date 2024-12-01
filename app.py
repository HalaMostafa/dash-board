import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(layout="wide")
df = pd.read_csv("data/Food_and_Nutrition__.csv")
st.write("original data shape: ",df.shape)

dietary_preference = ["Omnivore","Vegetarian","Vegan","Pescatarian"]
activity_level = ["Moderately Active","Lightly Active","Sedentary","Very Active""Extremely Active"]

# Function to reset the form inputs
def reset_form():
    current_data = df.copy()
    st.write(current_data.shape)

def supmitted():
    current_data = df.copy()
    current_data = current_data[(current_data["Activity Level"].isin(form_activity_level))&(current_data["Dietary Preference"].isin(form_dietary_preference))]
    st.write(current_data.shape)
# Create two columns with a 1:4 ratio
col1, col2 = st.columns([1, 4])

# Content for the first column (form)
with col1:
    st.header("Filters")
    with st.form("user_form"):
        # Form fields
        form_activity_level = st.multiselect("Activity Level",activity_level , default=None)
        form_dietary_preference = st.multiselect("Dietary Preference",dietary_preference , default=None)

        # Buttons
        submitted = st.form_submit_button("Submit")
        reset = st.form_submit_button("Reset")

# Content for the second column
with col2:
    if submitted:
        supmitted()
    else:
        reset_form()

