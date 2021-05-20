import os
import openai
from secrets import API_Token
from prompt import en_ru
translate_input = input("What to Translate: ")
openai.api_key = API_Token
response = openai.Completion.create(
engine="davinci",
prompt=en_ru + translate_input + "\nRussian: ",
temperature=0.5,
max_tokens=100,
top_p=1,
frequency_penalty=0,
presence_penalty=0,
stop=["###"]
)
print("Translation: " + response["choices"][0]["text"])