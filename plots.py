import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,4),
    columns= ['a','b','c','d'])
chart = alt.Chart(data).mark_circle().encode(
    x='a',y='b', tooltip= ['a','b']
)
st.altair_chart(chart, use_container_width=True)
data1 = pd.read_csv('/home/dell/Documents/Personal/streamlit/data/deadliest_earthquakes.csv')
# st.map(data1)


# to insert images 
st.image("/home/dell/Pictures/pexels-david-bartus-2379653.jpg")

# to add audio
#st.audio()

# to add vedio

st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k") # can add local or line vedio links


#flowchart
st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch
}
""")

# fig, ax = plt.subplots()
plt.scatter(data['a'],data['b'])
plt.title("Scatter plot")
st.pyplot(plt)



st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)