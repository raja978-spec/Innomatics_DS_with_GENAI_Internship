import streamlit as st
import google.generativeai as genai

key = open('.genimi.txt').read().strip()

genai.configure(api_key=key)

sys_admin = '''
You are a Python AI code reviewer, you should analyze all type of python
code and if the code has bugs you should give the description of that bug with the title 
called Bug Report(as bolder and bigger text)
and also you have to give the Fixed version of code with the title called
Fixed code (as bolder and bigger text), if the provided code will not have error you should give
appropriate message, You should give only the python code related response as a python
code reviewer, if the user asks any other questions or code which is not
related to python you have to say appropriate message like Iam a AI python code reviewer so
ask me question related to python with code.
'''

model = genai.GenerativeModel(model_name='models/gemini-2.0-flash-exp', system_instruction=sys_admin)

st.title("📝 An AI Code Reviewer")
code = st.text_area('Enter your python code here...')

generate_button = st.button('Generate')
is_generate_button_clicked = generate_button

if is_generate_button_clicked:
    output = model.generate_content(code).text
    st.title('Code Review')
    st.markdown(output)
