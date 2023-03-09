import streamlit as st

st.title("widgets")

if st.button("Subscribe"):
    st.write("Thnak you :smile:")


name = st.text_input("Name")
st.write(name)

address = st.text_area("enter your address")
st.write(address)

st.date_input("Enter a date")

st.time_input("Enter the time")

if st.checkbox("Accept to submit", value = False):
    st.write("Thank you")

v1 = st.radio("Colors",["red", "Blue", "Green"])
v2 = st.selectbox("Colors",["red", "Blue", "Green"])

st.write(v1,v2)

v3 = st.multiselect("Colors",["red", "Blue", "Green"])
st.write(v3)

st.slider("age",min_value= 10,max_value = 60, value = 10, step = 1)

st.number_input("BP",min_value= 80.0,max_value = 200.0, value = 100.0, step = 5.0)

# to upload a file

v4 = st.file_uploader("Upload a file")
st.image(v4)