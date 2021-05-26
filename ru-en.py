import os
import openai
from secrets import API_Token
from prompt import ru_en
translate_input = input("Что переводить: ")
openai.api_key = API_Token
response = openai.Completion.create(
engine="davinci",
prompt=ru_en + translate_input + "\nEnglish: ",
temperature=0.5,
max_tokens=100,
top_p=1,
frequency_penalty=0,
presence_penalty=0,
stop=["###"]
)
print("Перевод:" + response["choices"][0]["text"])