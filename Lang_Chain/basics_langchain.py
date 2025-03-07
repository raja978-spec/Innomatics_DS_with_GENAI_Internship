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



                     # PYDANTIC OUTPUT PARSER

Used to create custom parser with type validators.

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
class Song(BaseModel):
    name:str= Field(description='Name of the song')
    genre:str = Field(description='Name of the genre')
    singer_list:list = Field(description='Name of the singers list')
    no_of_signers: int = Field(...,description='No of singers')


output_parser = PydanticOutputParser(pydantic_object=Song)

prompt_templet = ChatPromptTemplate(
    messages=[
    ('system','Your a Song AI you have to give the name of the song, genre of the song and singers of the song OUTPUT_FORMAT:{o_format}'),
    ('user','What genre of songs is this {song_name}')
],
partial_variables = {'o_format': output_parser.get_format_instructions()}
)


API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=API_KEY)

chain = prompt_templet | model | output_parser

response = chain.invoke({'song_name':'kadhal psycho'})
print(response)

# name='Kadhal Psycho' genre='Indian Pop' singer_list=['Akash Ravikrishnan', 'Deepthi Suresh'] no_of_signers=2

# After specifying max_length validator the output of the genre is changed
# name='Kadhal Psycho' genre='Folk' singer_list=['Silambarasan TR', ' Roshini', ' G.V. Prakash Kumar'] no_of_signers=3 website_name='www.youtube.com' singer_age=30


If any of the specified validation is not meet for the model result the
it will give error

EX:

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
class Song(BaseModel):
    name:str= Field(description='Name of the song')
    genre:str = Field(description='Name of the genre', max_length=5)
    singer_list:list = Field(description='Name of the singers list')
    no_of_signers: int = Field(...,description='No of singers') #... specifies it is mandatory field
    website_name: str = Field(pattern=r'^www|http.com$', description='Give me the download link in this format')

    # this raise error
    singer_age: int = Field(gt=30, lt=31, description='Give the age of any one of the singer')


output_parser = PydanticOutputParser(pydantic_object=Song)

prompt_templet = ChatPromptTemplate(
    messages=[
    ('system','Your a Song AI you have to give the name of the song, genre of the song and singers of the song OUTPUT_FORMAT:{o_format}'),
    ('user','What genre of songs is this {song_name}')
],
partial_variables = {'o_format': output_parser.get_format_instructions()}
)


API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=API_KEY)

chain = prompt_templet | model | output_parser

response = chain.invoke({'song_name':'kadhal psycho'})
print(response)

ERROR:

. Got: 1 validation error for Song
singer_age
  Input should be greater than 30 [type=greater_than, input_value=30, input_type=int]


                          # JSON PARSER

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
class Song(BaseModel):
    name:str= Field(description='Name of the song')
    genre:str = Field(description='Name of the genre', max_length=5)
    singer_list:list = Field(description='Name of the singers list')
    no_of_signers: int = Field(...,description='No of singers') #... specifies it is mandatory field
    website_name: str = Field(pattern=r'^www|http.com$', description='Give me the download link in this format')
    singer_age: int = Field(gt=30, lt=35, description='Give the age of any one of the singer')

output_parser = JsonOutputParser(pydantic_object=Song)

prompt_templet = ChatPromptTemplate(
    messages=[
    ('system','Your a Song AI you have to give the name of the song, genre of the song and singers of the song OUTPUT_FORMAT:{o_format}'),
    ('user','What genre of songs is this {song_name}')
],
partial_variables = {'o_format': output_parser.get_format_instructions()}
)


API_KEY = open('.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=API_KEY)

chain = prompt_templet | model | output_parser

response = chain.invoke({'song_name':'kadhal psycho'})
print(response)


OUTPUT:

{'name': 'Kadhal Psycho', 'genre': 'Folk', 'singer_list': [], 'no_of_signers': 2, 'website_name': 'www.example.com', 'singer_age': 32}

'''

#                       LCEL, STREAM
'''
 LC- Langchain E- Extend L-Language

 It is pipe line used to chain prompt, model, output parser


 Stream - Gives output like chat gpt doesn't wait to generate whole
          response while invoke waits to generate whole response and
          then print it.

EX:

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

prompt_templates = ChatPromptTemplate(
    messages=[
        ('system','You are a AI research assistant, write good research paper with the user provided topic'),
        ('user','Generate research paper on {topic}')
    ]
)

API_KEY = open('.genimi.txt').read().strip()

model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')

strparser = StrOutputParser()

chain = prompt_templates | model | strparser

for chuck in chain.stream({'topic':'Transformers'}):
    print(chuck, end='')

#print(chain.invoke({'topic':"Transformers"}))



                TEMPERATURE

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt_templates = ChatPromptTemplate(
    messages=[
        ('system','You are a AI research assistant, write good research paper with the user provided topic'),
        ('user','Generate research paper on {topic}')
    ]
)

OPEN_API_KEY = open('.openai.txt').read().strip()
print(OPEN_API_KEY)
model = ChatOpenAI(api_key=OPEN_API_KEY, model_name="gpt-4o-mini",
                               temperature=0.0)

strparser = StrOutputParser()

chain = prompt_templates | model | strparser

for chuck in chain.stream({'topic':'Transformers'}):
    print(chuck, end='')

#print(chain.invoke({'topic':"Transformers"}))


                        # DEFAULT VALUES IN CUSTOM OUTPUT PARSER

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field

class Song(BaseModel):
    singer_name:list = Field(default=['empty'])
    no_of_singers:int = Field(default=1) 

obj = Song()
print(obj.singer_name)
outparser = StrOutputParser(pydantic_object=Song)

prompt_template = ChatPromptTemplate(
    messages=[
        ('system','You are Ai assistant'),
        ('human','give me list of singers of specified song {song_name} with outout format like this OUTPUT FORMAT: {outparser}')
    ],
    partial_variables = {'outparser': outparser}
)

API_KEY = open('.genimi.txt').read().strip()


model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')

chain = prompt_template | model | outparser

r=chain.invoke({'song_name':'Kal Ho Naa Ho'})
print('Processing....')
print(r)

OUTPUT:

['empty']
Processing....
Okay, I understand. Please provide me with the song title you're interested in. 
Once you provide the song, I will give you the list of singers in the 
following format:

**OUTPUT FORMAT:**

*   **Singer 1:** \[Name of Singer 1]
*   **Singer 2:** \[Name of Singer 2]
*   **Singer 3:** \[Name of Singer 3]
*   ...and so on...

For the song "Kal Ho Naa Ho", here's the information:

**OUTPUT FORMAT:**

*   **Singer 1:** Sonu Nigam
'''

#             MEMORY SPACE TO CHAT PREVIOUS CHATS
'''
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI Chat bot'),

        # Place holder for chat history
        # optional True makes the chat_history is
        # optional to call
        MessagesPlaceholder(variable_name='chat_history', optional=True),

        ('human',"{human_input}")
    ]
)

API_KEY = open('Lang_Chain/.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = chat_template | model | output_parser
print(type(chain)) # all three pipe line have different types
                   # but when we chained all the pipeline
                   # it will gives as runnable. For memory
                   # also we have to create custom runnables.


# INITIALIZE THE MEMORY
from langchain_core.runnables import RunnableLambda

# RunnableLambda is the class helps to create an custom runnables
# any python function passed to this class will become runnables
# EX: def sum(e): return e-1 
# custom_runnable = RunnableLambda(sum)
# without converting our function to runnable sequuence we
# can't chain it with | pipe symbol

# Below is actual example where we converted
# get_chat_history to runnable.

memory_buffer = {'history':[]}

def get_chat_history(human_input):
    return memory_buffer['history']

runnable_get_history = RunnableLambda(get_chat_history)

# Creating the actual chain with the runnables

from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough.assign(chat_history = runnable_get_history) | chat_template | model | output_parser


#   SAVING TO MEMORY
from langchain_core.messages import HumanMessage, AIMessage

while True:
    query = {'human_input':input('*User: ')}

    if query['human_input'] == 'q':
        break

    response = chain.invoke(query)
    print('*AI: ', response)
    memory_buffer['history'].append(HumanMessage(content=query['human_input']))
    memory_buffer['history'].append(AIMessage(content=response))

OUTPUT:

*User: hi my name is raja
*AI:  Hello Raja, it's nice to meet you! How can I help you today?
*User: explain ml in 1 line
*AI:  Machine learning enables computers to learn from data without explicit programming.
*User: what is my name
*AI:  Your name is Raja.
*User:

Now the model it capable to memorize previous chat
'''

#             CONNECTING SQL LITE TO STORE CHAT
'''
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import SQLChatMessageHistory

chat_template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI Chat bot'),

        MessagesPlaceholder(variable_name='chat_history', optional=True),

        ('human',"{human_input}")
    ]
)

API_KEY = open('Lang_Chain/.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()


def get_session_message_from_db(session_id):
    chat_message_history = SQLChatMessageHistory(
        session_id= session_id,
        connection="sqlite:///chats_data/sqlite.db"
    )
    return chat_message_history


chain = chat_template | model | output_parser

from langchain_core.runnables.history import RunnableWithMessageHistory

conversation_chain = RunnableWithMessageHistory(
    chain,
    get_session_message_from_db,
    input_messages_key='human_input',
    history_messages_key='chat_history'

)


while True:
    user_id = "thatguy"
    config = {'configurable':{'session_id': user_id}}

    input_propmt = {'human_input':input('*User: ')}
    response = conversation_chain.invoke(input_propmt, config=config)


    if input_propmt['human_input'] == 'q':
        break

    print('*AI: ', response)
'''


#                     MODEL RETRIEVAL 
'''
It is helps models to updated with latest information, without the new latest information retrieval model will always give old results.
The model will give hallucinated answer.
For overcome this issue RAG is used here.
On RAG we attached a knowledge base the model from that knowledge base all the latest info will be retrieved.
We will give place holder to hold the latest info and that will be retrie

In the above approach we have one problem that is when a size of knowledge base increases then the prompt goes to model will be huge
EX: Assume knowledge base containing the 100 various document each have 1000+ pages


Model will not process whole knowledge base information because it has limited constant window that will take some size of data from knowledge base instead of taking whole data. 
To over come this issue chunking is used.
On chunking we will pass needed part of file to give correct answer to the user question by we converting whole text knowledge base values to numeric vectors and that vectors are will be stored in a vector DB.

User input also are gets converted into numeric representation and that numeric user input are passed to vector DB to find the correct answer for the user query from those collection of chunks. To identify the similar file from vector DB along with converted user input we have use another method called cosine similarity (works well for high dim data). And that founded chunk are the only info which are passed to model.
Below is the image which elaborates the above theory process.

'''     
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

chat_template = ChatPromptTemplate(
    messages=[
        ('system','You are a AI assistant, You have the access to the following data, Given a human input if you dont have answer to the question you should refer following data before answering the question: {new_data}'),
        MessagesPlaceholder(variable_name='chat', optional=True),
        ('user','{human_input}')
    ],
    partial_variables = {'new_data':None}
)

API_KEY = open('Lang_Chain/.genimi.txt').read().strip()
model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')

outputparser = StrOutputParser()


chain = chat_template | model | outputparser


while True:
    user_input = input('*User: ')
    response = chain.invoke({'human_input': user_input})
    if user_input == 'q':
        print('*AI: bye have a nice day')
        break
    print("*AI: ", response)


