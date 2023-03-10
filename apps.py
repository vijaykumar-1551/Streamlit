import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from  plotly import offline as plo
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np
import time

# import plotly as
data = pd.read_csv("/home/dell/Documents/Personal/streamlit/data/Salary_Data.csv")

x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))
st.title("Salary Predictor")

nav = st.sidebar.radio("Navigate",["Home","Predict", "Contribute"])
if nav == "Home":
    st.image("/home/dell/Documents/Personal/streamlit/data/salary.jpg" )
    if st.checkbox("Show data table"):
        st.table(data)

    graph = st.selectbox("Type of Graph", ["Non-Interactive", "Interactive"])
    val= st.slider("Filter data by years", 0, 11)

    data = data.loc[data["YearsExperience"]>= val]

    if graph == "Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot(plt)
    if graph== "Interactive":
        # layout = go.Layout(
        #     xaxis = dict(range= [0,16]),
        #     yaxis = dict(range = [0,200000])
        # )
        fig = go.Figure(data = go.Scatter(x = data["YearsExperience"],y = data["Salary"], mode = "markers"))
        st.plotly_chart(fig)

if nav == "Predict":
    st.header("Check Salary according to yours experience")
    val = st.number_input("Enter your experience",0.00, 20.00, step = 0.25)
    val1 = np.array(val).reshape(1,-1)
    pred = lr.predict(val1)[0]

    if st.button("predict"):
        st.success(f"Your predicted salary is {round(pred)}")

if nav == "Contribute":
    st.header("Contribute to our database")
    ex = st.number_input("Enter your experience",0.00, 20.00)
    sal = st.number_input("Enter your salary",0.00, 10000000.00, step= 1000.00)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex], "Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("/home/dell/Documents/Personal/streamlit/data/Salary_Data.csv", mode = 'a',header = False, index =False)
        st.success("Submitted")