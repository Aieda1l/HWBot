import openai
import subprocess
from colorama import Fore, Style
import pwinput
import json

with open("config.json") as json_file:
    openai.api_key = json.load(json_file).get("api_key")

model_engine = 'text-davinci-003'
  
def askquestion(question, engine):
  completion = openai.Completion.create(
    engine = model_engine,
    prompt = question,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,
  )

  response = completion.choices[0].text
  print(response + '\n')

while True:
  question = input("Input question: ")
  if question == "read file":
    lines = ""
    with open("input.txt") as f:
      data = f.readlines()
      lines = " ".join(data)
    f.close()
    askquestion(lines, model_engine)
  else:
    askquestion(question, model_engine)