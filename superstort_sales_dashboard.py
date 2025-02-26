import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from layout import figure_defaults


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
        "segment": st.multiselect("Segment", segment, default=None),
        "category": st.multiselect("Category", category, default=None),
        "start_date": st.date_input("Order Start Date", value=None),
        "end_date": st.date_input("Order End Date", value=None)
    }


df = pd.read_csv("data/train.csv")


@figure_defaults()
def create_figure(df, options):
    """No. of orders per period of time"""
    df["Order Date"] = pd.to_datetime(df["Order Date"], format='mixed')
    groupby = options["groupby"]
    period = df["Order Date"].dt.to_period(groupby).astype(str)
    count = df.groupby(period)["Order ID"].nunique().reset_index()
    return go.Figure(go.Scatter(x=count["Order Date"], y=count["Order ID"]))


no_orders_per_period = create_figure(
    df, {"title": "No. Of Orders Per Period", "groupby": "q", "start_date": "2015-01-01", "end_date": "2016-12-31"})


@figure_defaults()
def create_figure(df, option):
    """ship modes"""
    count = df["Ship Mode"].value_counts().reset_index()
    return go.Figure(
        data=[go.Pie(labels=count["Ship Mode"], values=count["count"])])


ship_modes = create_figure(df, {"title": "Ship Mode"})


@figure_defaults()
def create_figure(df, options):
    df["Order Date"] = pd.to_datetime(df["Order Date"], format='mixed')
    groupby = options["groupby"]
    period = df["Order Date"].dt.to_period(groupby).astype(str)
    count = df.groupby(period)["Sales"].mean().reset_index()
    return go.Figure(go.Scatter(x=count["Order Date"], y=count["Sales"]))


avg_sales = create_figure(df, {"title": "Avg. Sales", "groupby": "q",
                          "start_date": "2015-01-01", "end_date": "2016-12-31"})


@figure_defaults()
def create_figure(df, options):
    df["Order Date"] = pd.to_datetime(df["Order Date"], format='mixed')
    groupby = options["groupby"]
    period = df["Order Date"].dt.to_period(groupby).astype(str)
    # count = df.groupby([period,"Category"])["Sales"].mean().reset_index()
    table = pd.pivot_table(df, values='Sales', index=[period],
                           columns=['Category'], aggfunc="mean")

    data = []
    for col in table.columns:
        data.append(
            go.Bar(
                x=table.index,
                y=table[col],
                name=col
            )
        )
    fig = go.Figure(data)
    return fig


avg_sales_category = create_figure(
    df, {"title": "Avg. Sales", "groupby": "q", "start_date": "2015-01-01", "end_date": "2016-12-31"})
