#                       API KEY
'''
It is needed to access and use gemini AI models in local machine.
Refer Day-10 internship notes(Create GEMINI API KEY) to generate
api key
'''

#           BASIC CODE WITH SYSTEM INSTRUCTIONS ATTRIBUTE

'''
import google.generativeai as geminiai
from IPython.display import Markdown

key = open('key/.genimi.txt').read()
geminiai.configure(api_key=key.strip())

# Gives the name of all the availabel models in gemini
# for i in geminiai.list_models():
#     print(i)

# models/gemini-2.0-flash-exp is one of the model
# system_instruction act as a administrative settings 
# that forces model to give response in specific topic

sys_prompt = "
You are a helpful data science tutor, You can only resolve data science
related quires, In case if someone ask quires which are not data
science, politely tell them to ask relevant quires only
"

model = geminiai.GenerativeModel(model_name='models/gemini-2.0-flash-exp', system_instruction=sys_prompt)


user_prompt = "What is the use of paracetamol?"

# It will not generate fo this prompt
content = model.generate_content(user_prompt)
result = Markdown(content.text) # Pretty text output

print(content.text)

# OUTPUT: I am a data science tutor. Please ask me questions related to data science.
'''

import google.generativeai as geminiai
from IPython.display import Markdown

key = open('key/.genimi.txt').read()
geminiai.configure(api_key=key.strip())

# Gives the name of all the availabel models in gemini
# for i in geminiai.list_models():
#     print(i)

# models/gemini-2.0-flash-exp is one of the model
# system_instruction act as a administrative settings 
# that forces model to give response in specific topic

sys_prompt = '''
You are a helpful data science tutor, You can only resolve data science
related quires, In case if someone ask quires which are not data
science, politely tell them to ask relevant quires only
'''

model = geminiai.GenerativeModel(model_name='models/gemini-2.0-flash-exp', system_instruction=sys_prompt)


user_prompt = "What is the use of paracetamol?"

# It will not generate fo this prompt
content = model.generate_content(user_prompt)
result = Markdown(content.text) # Pretty text output

print(content.text)

# OUTPUT: I am a data science tutor. Please ask me questions related to data science.