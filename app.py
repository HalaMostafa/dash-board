import streamlit as st
import pandas as pd
from filters import filter_selected_options
import superstort_sales_dashboard as dashboard

# Set the page configuration
st.set_page_config(layout="wide")

get_form_options = dashboard.get_form_options
filter_data = dashboard.filter_data


def reset_form():
    current_data = dashboard.df
    st.write(current_data.shape)


def supmitted(form_options):
    filtered_form_options = filter_selected_options(form_options)
    filtered_data = filter_data(dashboard.df, filtered_form_options)
    st.write(filtered_data.shape)


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
        supmitted(form_options)
    else:
        reset_form()
