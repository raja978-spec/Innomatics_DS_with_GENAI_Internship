#           INTRO
'''
Streamlit is an open-source Python library that allows you 
to build interactive web applications for data science and 
machine learning with minimal code. It is designed to 
be simple and fast, enabling developers to create powerful 
UI components using only Python scripts.

Key Features of Streamlit
✅ Easy to Use – No need to write HTML, CSS, or JavaScript. 
Just use Python.

✅ Interactive Widgets – Add sliders, buttons, 
file uploads, etc., with simple function calls.

✅ Live Code Updates – Automatically updates when the 
script changes, making development fast.

✅ Built-in Data Visualization – Supports matplotlib, plotly, 
seaborn, and altair charts natively.

✅ Deployment Ready – Easily deploy apps to the web using 
Streamlit Cloud, Docker, or other services.

pip install streamlit

'''

#                 BASIC PROGRAM
import streamlit as st
st.title('Hello from stremalit')
text = st.text_area('Type anything..')
if st.button('click'): st.markdown(text)    