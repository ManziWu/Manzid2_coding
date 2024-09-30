import streamlit as st

st.header("Test Application")

if "name" not in st.session_state:
    st.session_state.name = None

st.session_state.name = st.text_input("what's ur name?")

if "age" not in st.session_state:
    st.session_state.age = None

st.session_state.age = st.text_input("How old are u?")

if st.button("Say Hi"):

    st.write(f"Hi,{st.session_state.name}!")

    if int(st.session_state.age) <= 24:
        st.write("you were born this millennium")
    else:
        st.write("you were born last millennuim")

