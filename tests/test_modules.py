import streamlit as st
import pytest
from filters import filter_selected_options


def get_form_options():
    """This function creates a form using various Streamlit input widgets,
    with all default values set to None until the user interacts with them.
    """

    # Sample options for selection
    options_list = ["Option A", "Option B", "Option C"]

    return {
        "text_input": st.text_input("Enter Text:", value=None),
        # "textarea": st.text_area("Enter Multi-line Text:", value=None),
        "number_input": st.number_input(
            "Choose a Number:", min_value=0, max_value=100, value=None
        ),
        # "slider": st.slider(
        #     "Slide to Select a Value:", min_value=1, max_value=100, value=None
        # ),
        "selectbox": st.selectbox(
            "Select an Option:", options=[""] + options_list, index=0
        ),
        "multiselect": st.multiselect(
            "Select Multiple Options:", options=options_list
        ),
        "radio": st.radio("Choose One:",  options_list, index=0),
        "checkbox": st.checkbox("Check if True:", value=None),
        "date_input": st.date_input("Pick a Date:", value=None),
        # "time_input": st.time_input("Pick a Time:", value=None),
        # "color_picker": st.color_picker("Pick a Color:", value=None),
        # "file_uploader": st.file_uploader("Upload a File:"),
    }


def test_filter_selected_options_complete():
    """test nothing to filter when all input widgets have values ereased by filter selected data function
    """
    data = {
        "text_input": "text",
        "number_input": 10,
        "selectbox": "Option A",
        "multiselect": ["Option B", "Option C"],
        "radio": "Option B",
        "checkbox": True,
        "date_input": "datetime.date(2024, 12, 24)"
    }
    filtered_data = filter_selected_options(data)
    assert data == filtered_data


def test_filter_selected_options_non_complete():
    """test nothing to filter when some input widgets with None value 
    """
    user_input_data = {
        "text_input": None,
        "number_input": 10,
        "selectbox": None,
        "multiselect": ["Option B", "Option C"],
        "radio": "Option B",
        "checkbox": True,
        "date_input": None
    }
    expected_filtered_data = {
        "number_input": 10,
        "multiselect": ["Option B", "Option C"],
        "radio": "Option B",
        "checkbox": True,
    }
    function_filtered_data = filter_selected_options(user_input_data)
    assert expected_filtered_data == function_filtered_data
