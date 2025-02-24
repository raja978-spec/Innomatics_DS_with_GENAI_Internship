from openai import OpenAI

key = open(r'GENAI\key\.openai.txt').read().strip()
print(key)

openAPIModel = OpenAI(api_key=key)

for i in openAPIModel.models.list():
    print(i)