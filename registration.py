import streamlit as st

st.title("Registration form")

first, last = st.columns(2)
first.text_input("First name")
last.text_input("Last name")

email,mob = st.columns([3,1])
email.text_input("Email")
mob.text_input("Mobile number")

username,password, pw2 = st.columns(3)
username.text_input("Username")
password.text_input("Password", type ="password")
pw2.text_input("Re-enter password", type = "password")

ch,bl,sub = st.columns(3)
ch.checkbox("I agree")
sub.button("submit")


