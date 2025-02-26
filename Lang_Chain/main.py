
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

#                 WHOLE CODE

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

chat_prompt = ChatPromptTemplate(
    messages=[
        ('system','You are a AI travel agent user will give you the source and destination location you have to give them the cost of the travel by bus,train,flight or mach more'),
        ('user', 'I want to travel from {source} to {destination} by {travel_method}')
    ],
    partial_variables={'travel_method':'bus, train, flight'}
)

model = GoogleGenerativeAI(api_key='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')

response_formatter = StrOutputParser()

chain = chat_prompt | model | response_formatter

user_input = input('Enter source destination and travel method: ').split(' ')
args = {}
args['source'] = user_input[0]
args['destination'] = user_input[1]
args['travel_method'] = user_input[2]

response = chain.invoke(args)

print(response)