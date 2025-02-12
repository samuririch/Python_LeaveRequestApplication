import streamlit as st
import functions
import sqlConnect

def my_function():
    functions.loadMainBook(option)
    st.session_state.button_clicked = True

def db_connect():
    sqlConnect.connect_to_db('EmployeeRecords.db')

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.button("Search", on_click=my_function, disabled=st.session_state.button_clicked):
    pass

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.button("Connect To DB", on_click=my_function, disabled=st.session_state.button_clicked):
    pass

#python -m streamlit run main.py
st.title = ("My Leave Application")
st.subheader("Welcome to the Leave Request Application")

st.write("Please select an Employee:")
option = st.selectbox('Please select an Employee:', ('Select','Samuel', 'Aimee'))





#st.button("Search", on_click=my_function())

