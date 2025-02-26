# #                 CODE FOR AI TRAVEL AGENT

# import ai_responser
# import streamlit as st

# st.set_page_config(page_title="AI Travel Partner", page_icon="✈️", layout="centered")

# st.markdown(
#     """
#     <style>
#     .big-font { font-size:24px !important; font-weight:bold; color:#2E86C1; }
#     .small-font { font-size:16px !important; color:#5D6D7E; }
#     .stButton>button { background-color:#2E86C1; color:white; font-size:18px; padding:10px; border-radius:10px; }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown('<p class="big-font">🌍 AI Travel Partner</p>', unsafe_allow_html=True)

# with st.form("travel_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         source = st.text_input("🏙️ Source Location", placeholder="Enter starting location")
#     with col2:
#         destination = st.text_input("📍 Destination Location", placeholder="Enter destination")

#     travel_by = st.selectbox("🚗 Travel By", ["Bus", "Train", "Flight"])

#     date = st.date_input("📅 Travel Date")
#     time = st.time_input("⏰ Travel Time")

#     submit_btn = st.form_submit_button("🔍 Find Cost")

# if submit_btn:
#     time_and_date = f"{date.strftime('%d/%m/%Y')} {time.strftime('%I:%M %p')}"

#     response = ai_responser.find_cost(source, destination, time_and_date, travel_by)

#     if response:
#         st.success(response)
#     else:
#         st.error("⚠️ Unable to fetch travel cost. Please check the inputs.")


#      PROMPT TEMPLATE AND CHAT PROMPT TEMPLATE
'''
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

propmt = ChatPromptTemplate.from_messages([
    ('system', 'You are a AI Asstient for python code reviewer'),
    ('human', 'Tell me about {info}')
    ])

args = {'info':'World'}
u = propmt.invoke(args)
# print(u.to_string())
# print(u.to_messages())

p = ChatPromptTemplate(
    messages=[
    ('system', 'You are a AI Asstient for python code reviewer'),
    ('human', 'Tell me about {info_1} {info_2}')
    ],
    partial_variables = {'info_2': 'AI'} # puts defualt value to info_2
)
args = {'info_1':'World'}

#print(p.invoke(args))
# OUTPUT: content='Tell me about World AI'


p = PromptTemplate.from_template('Hello from {info}')
args = {'info':'World'}

print(p.invoke(args))

'''

#                 TYPES OF OUTPUT PARSER
'''
 Outputs from model can be formatted as csv, list, string

 EX for list output:

from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

comma = CommaSeparatedListOutputParser() # gives list output
str = StrOutputParser()# gives str output

template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI Chef you have to give list of ingredient to cook the given recipe Output Format Instruction: {output_format}'),
        ('human','Give me list of ingredient to cook {food_name}')
    ],
    partial_variables = {'output_format': comma.get_format_instructions()}
) 

API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')


chain = template | model | comma

print(chain.invoke({'food_name':'rice'}))

# OUTPUT: ['rice', 'water']


                         #  PARSE METHOD

We can parse the model response to the commaseperated parser
to get the output in list

from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

comma = CommaSeparatedListOutputParser() # gives list output
str = StrOutputParser()# gives str output

template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI Chef you have to give list of ingredient to cook the given recipe Output Format Instruction: {output_format}'),
        ('human','Give me list of ingredient to cook {food_name}')
    ],
    partial_variables = {'output_format': str}
) 

API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')


chain = template | model | str
response = chain.invoke({'food_name':'rice'})

print(comma.parse(response))
# OUTPUT: ['*   1 cup long-grain white rice', '*   2 cups water', '*   1/2 teaspoon salt (optional)']



                          #DATE OUTPUT PARSER

code not working

from langchain_core.output_parsers import StrOutputParser, DatetimeOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

date = DatetimeOutputParser()

template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI assistant to give the exact time and date of past historical event which user asks Output Format Instruction: {output_format}'),
        ('human','Give me the date and time {event}')
    ],
    partial_variables = {'output_format': date.get_format_instructions()}
) 

API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')


#chain = template | model | comma
chain = template | model | date
response = chain.invoke({'event':'Independence day of India'})

print(response)



'''
from langchain_core.output_parsers import StrOutputParser, DatetimeOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

date = DatetimeOutputParser()

template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI assistant to give the exact time and date of past historical event which user asks Output Format Instruction: {output_format}'),
        ('human','Give me the date and time {event}')
    ],
    partial_variables = {'output_format': date.get_format_instructions()}
) 

API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')


#chain = template | model | comma
chain = template | model | date
response = chain.invoke({'event':'Independence day of India'})

print(response)

