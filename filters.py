import pandas as pd
import datetime


def date_filter(df, col_name: str, form_options: dict):
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
    if "start_date" in form_options:
        df = df.loc[
            df[col_name]
            >= datetime.datetime.strptime(str(form_options["start_date"]), "%Y-%m-%d")
        ].copy()
    if "end_date" in form_options:
        df = df.loc[
            df[col_name]
            <= datetime.datetime.strptime(str(form_options["end_date"]), "%Y-%m-%d")
        ].copy()
    return df


def get_complete_xaxis(form_options: dict, df, col_name: str, options: dict):
    """the purpose of this function is to get min and max date in the filtered df,
    then pass them to the options that is parameter for create_figure
    in case of x-axis is periods date"""
    df[col_name] = pd.to_datetime(df[col_name], errors="coerce").dt.normalize()
    min_date, max_date = df[col_name].min(), df[col_name].max()
    start_date = form_options.get("start_date", min_date)
    end_date = form_options.get("end_date", max_date)
    frequant = options["groupby"]
    return pd.DataFrame(
        {
            "x": pd.period_range(
                start=start_date,
                end=end_date,
                freq=frequant,
            )
        },
    )


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
