from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


def DSTutor(user_input): 
    chat_prompt = ChatPromptTemplate(
        messages=[
            ('system','''
            You are an AI Data Science Tutor, designed to assist users with data science-related topics.  
            Your role is to provide accurate, informative, and insightful responses to questions related to  
            machine learning, deep learning, statistics, data analysis, and other data science domains.  

            **Guidelines:**  
            - Only respond to **data science-related** queries.  
            - If a user asks something **unrelated to data science**, politely guide them back to relevant topics  
              without explicitly stating, "I am a Data Science tutor."  
            - If a user requests their **chat history**, retrieve and display it without modifying or summarizing  
              the previous interactions.  

            Keep your responses concise, structured, and easy to understand. 
            '''
            ),
            (
                MessagesPlaceholder(variable_name='chat_history', optional=True)
            ),
            ('human','{human_input}')
        ]
    )

    API_KEY = open('.genimi.txt').read().strip()
    
    model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-1.5-flash-latest')

    output_str = StrOutputParser()

    chain = chat_prompt | model | output_str

    def get_history_chats_from_db(session_id):
            chat_histories = SQLChatMessageHistory(session_id=session_id, 
                                               connection='sqlite:///chats_data/history.db')
            return chat_histories
       
    chain_with_chat_history_db = RunnableWithMessageHistory(
        chain,
        get_history_chats_from_db,
        input_messages_key='human_input',
        history_messages_key='chat_history'
    )
    sess_id = {'session_id': "raja"}
    config = {'configurable': sess_id}
    response = chain_with_chat_history_db.invoke({'human_input':user_input}, config=config)
    return response
