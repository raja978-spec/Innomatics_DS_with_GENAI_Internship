#                       WHAT IS GENAI
'''
 It is a application that uses existing model used
 on website like chatgpt.
'''

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


#            EXAMPLE GEMINI AI CODE FOR IMAGE MODEL
'''
import google.generativeai as geminiai
from PIL import Image
import matplotlib.pyplot as plt

# Configure API key
key = open('GENAI/key/.genimi.txt').read()
geminiai.configure(api_key=key.strip())

# Load image
img = Image.open('GENAI/image.jpg')

# Display image (optional)
plt.imshow(img)
plt.axis('off')  # Hide axes for better visualization
plt.show()

# Define the system instruction (text prompt)
sys_prompt = "Analyze the given image and describe its contents."

# Initialize the Gemini model
model = geminiai.GenerativeModel(model_name='models/gemini-1.5-flash')

# Generate content with both text and image
response = model.generate_content([img, sys_prompt])

# Print response
print(response.text)

'''

import google.generativeai as geminiai
from PIL import Image
import matplotlib.pyplot as plt

# Configure API key
key = open('GENAI/key/.genimi.txt').read()
geminiai.configure(api_key=key.strip())

# Load image
img = Image.open('GENAI/image.jpg')

# Display image (optional)
plt.imshow(img)
plt.axis('off')  # Hide axes for better visualization
plt.show()

# Define the system instruction (text prompt)
sys_prompt = "Analyze the given image and describe its contents."

# Initialize the Gemini model
model = geminiai.GenerativeModel(model_name='models/gemini-1.5-flash')

# Generate content with both text and image
response = model.generate_content([img, sys_prompt])

# Print response
print(response.text)
