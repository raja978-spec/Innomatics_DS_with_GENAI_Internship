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


