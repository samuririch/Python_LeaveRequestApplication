import streamlit as st
import functions

#python -m streamlit run main.py
st.title = ("My Leave Application")
st.subheader("Welcome to the Leave Request Application")

st.write("Please select an Employee:")
option = st.selectbox('Please select an Employee:', ('Select','Samuel', 'Aimee'))

def my_function():
    functions.loadMainBook(option)
    st.session_state.button_clicked = True

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.button("Search", on_click=my_function, disabled=st.session_state.button_clicked):
    pass



#st.button("Search", on_click=my_function())

