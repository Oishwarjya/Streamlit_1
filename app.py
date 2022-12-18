import streamlit as st
import plotly.graph_objects as go



#------- SETTINGS-----------

incomes = [ "Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Savings"]
currency = "USD"
page_title = "Income and Expenses"
page_icon = ":money_with_wings:"  #emojis: 
layout = "centered"

st.set_page_config(page_title= page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " +page_icon)