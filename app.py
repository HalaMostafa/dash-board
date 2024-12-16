import streamlit as st
import pandas as pd
from filters import date_filter, filter_selected_options
from superstort_sales_dashboard import get_form_options
# Set the page configuration
st.set_page_config(layout="wide")
# df = pd.read_csv("data/Food_and_Nutrition__.csv")
df = pd.read_csv("data/train.csv")

st.write("original data shape: ", df.shape)

# Function to reset the form inputs


def reset_form():
    current_data = df.copy()
    st.write(current_data.shape)


def supmitted():
    st.write(form_options)
    st.write(filter_selected_options(form_options))


# Create two columns with a 1:4 ratio
col1, col2 = st.columns([1, 4])

# Content for the first column (form)
with col1:
    st.header("Filters")
    with st.form("user_form"):
        # Form fields
        form_options = get_form_options()
        # Buttons
        submitted = st.form_submit_button("Submit")
        reset = st.form_submit_button("Reset")

# Content for the second column
with col2:
    if submitted:
        supmitted()
    else:
        reset_form()
