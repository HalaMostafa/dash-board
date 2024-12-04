import streamlit as st




def get_form_options():
    """this function creats static filter per project dashboard
    returns python dictionary contain streamlit form
    """
    ship_mode = [
        "Second Class",
        "Standard Class",
        "First Class",
        "Same Day",
        ]
    segment = [
        "Consumer",
        "Corporate",
        "Home Office",
        ]
    category = [
        "Furniture",
        "Office Supplies",
        "Technology",
        ]
    
    return {
            "ship_mode": st.multiselect("Ship Mode", ship_mode, default=None),
            "segment":st.multiselect("Segment",segment , default=None),
            "category":st.multiselect("Category",category , default=None),
            "start_date": st.date_input("Order Start Date",value = None),
            "end_date":st.date_input("Order End Date",value = None)
        }