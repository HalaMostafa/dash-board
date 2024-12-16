import pandas as pd
import datetime


def date_filter(df, col_name: str, options: dict):
    """filter dataframe based period of time
    Args:
        df: 
            pandas dataframe.
        col_name:
            (string) column name will used to filter data based on it.
        options:
            (python dictionay)
    Returns:
        df:

    """
    df[col_name] = pd.to_datetime(df[col_name], errors="coerce").dt.normalize()
    if options["start_date"] != None:
        df = df.loc[
            df[col_name]
            >= datetime.datetime.strptime(str(options["start_date"]), "%Y-%m-%d")
        ].copy()
    if options["end_date"] != None:
        df = df.loc[
            df[col_name]
            <= datetime.datetime.strptime(str(options["end_date"]), "%Y-%m-%d")
        ].copy()
    return df


def filter_selected_options(form_data):
    """Filters the form data to include only fields with user-selected values."""
    return {
        key: value
        for key, value in form_data.items()
        if isinstance(value, list)
        and value
        or not isinstance(value, list)
        and value
    }
