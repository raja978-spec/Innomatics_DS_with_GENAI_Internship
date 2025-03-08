import streamlit as st
from main import DSTutor

st.set_page_config(page_title="DS Tutor", page_icon="📚", layout="centered")

st.title("🤖 AI Data Science Tutor")
st.write("Ask any **Data Science** related question, and I’ll help you out!")

   
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

        with st.spinner('Thinking...'):
             ai_response = DSTutor(user_prompt)

        with st.chat_message('ai'):
            st.markdown(ai_response)
        st.session_state.messages.append({'role':'ai','content':ai_response})