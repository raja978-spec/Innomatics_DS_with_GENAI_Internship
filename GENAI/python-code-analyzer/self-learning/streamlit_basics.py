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
'''
import streamlit as st
st.title('Hello from stremalit')
text = st.text_area('Type anything..')
if st.button('click'): st.markdown(text)    
'''


#             BASIC CHAT APP REQUIREMENTS

import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_prompt = st.chat_input('Enter your questions')

if user_prompt:
    with st.chat_message('user'):
        st.markdown(user_prompt)
    st.session_state.messages.append({'role':'user','content':user_prompt})

    ai_response = f'Echo {user_prompt}'

    with st.chat_message('ai'):
        st.markdown(ai_response)
    st.session_state.messages.append({'role':'ai','content':ai_response})