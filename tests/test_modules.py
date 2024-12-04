import streamlit as st

def get_form_options():
    """This function creates a form using various Streamlit input widgets,
    with all default values set to None until the user interacts with them."""
    
    # Sample options for selection
    options_list = ["Option A", "Option B", "Option C"]
    date_default = None  # No default date
    
    # Create form inputs with defaults set to None
    form_inputs = {
        "text_input": st.text_input("Enter Text:", value="") or None,
        "textarea": st.text_area("Enter Multi-line Text:", value="") or None,
        "number_input": st.number_input("Choose a Number:", min_value=0, max_value=100, value=None),
        "slider": st.slider("Slide to Select a Value:", min_value=1, max_value=100, value=None),
        "selectbox": st.selectbox("Select an Option:", options=[""] + options_list, index=0) or None,
        "multiselect": st.multiselect("Select Multiple Options:", options=options_list) or None,
        "radio": st.radio("Choose One:", options=[""] + options_list, index=0) or None,
        "checkbox": st.checkbox("Check if True:", value=None) or None,
        "date_input": st.date_input("Pick a Date:", value=date_default) or None,
        "time_input": st.time_input("Pick a Time:", value=None) or None,
        "color_picker": st.color_picker("Pick a Color:", value=None) or None,
        "file_uploader": st.file_uploader("Upload a File:"),
    }
    
    # # Ensure all fields default to None if the user hasn't interacted
    # for key, value in form_inputs.items():
    #     if isinstance(value, (str, list)) and not value:
    #         form_inputs[key] = None
    #     elif value == "":
    #         form_inputs[key] = None
    
    return form_inputs
