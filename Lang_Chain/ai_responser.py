from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


def find_cost(source, destination, time, travel_by):

    chat_prompt = ChatPromptTemplate(
    messages=[
        ('system', "You are an AI travel agent. The user will provide a source and destination, and you will provide the cost of travel for different options such as bus, train, or flight."),
        ('user', "I want to travel from {source} to {destination} by {travel_method} on {date_time}.")
    ],
    partial_variables={'travel_method': 'bus, train, flight', 'date_time': 'today'}
    )

    API_KEY = open('.genimi.txt').read().strip()
    model = ChatGoogleGenerativeAI(api_key=API_KEY, model='gemini-2.0-flash-exp')

    response_formatter = StrOutputParser()

    chain = chat_prompt | model | response_formatter

    args = {}
    args['source'] = source
    args['destination'] = destination
    args['travel_method'] = travel_by
    args['date_time'] = time

    response = chain.invoke(args)

    return(response)
