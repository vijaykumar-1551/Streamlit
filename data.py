import streamlit as st
import pandas as pd
import numpy as np
import time


a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":"yash",
    "age":34,
    "place": "bengaluru"
}

data = pd.read_csv("/home/dell/Documents/Personal/streamlit/data/deadliest_earthquakes.csv")

st.dataframe(data,width = 300,height =500) # shows the table with scoll bar
st.table(data) # displays the entire table
st.json(dic)  # to show the data in dictionary format
st.write(dic)

@st.cache_data
def ret_time(r):
    time.sleep(5)
    return time.time()


if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))

