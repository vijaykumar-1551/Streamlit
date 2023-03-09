import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)],
    "Power_3":[x**3 for x in range(1,11)]
}
rad = st.sidebar.radio("navigation",["Home","About"])
if rad =="Home":
    df = pd.DataFrame(data = data)

    col =st.sidebar.multiselect("select a column",df.columns)

    plt.plot(df['num'], df[col])
    st.pyplot(plt)
if rad == "About": 
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()

    st.error("Error")
    st.success("Show success")
    st.info("information")
    st.exception(RuntimeError("This is runtime error"))
    st.warning("this is a warning")

    st.markdown("# Hi Welcome :smile:")