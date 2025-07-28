from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 
client = OpenAI()  

stream = client.responses.create(
    model="gpt-4o",
    input = "Make python code for factorial",
    stream=True
)

for event in stream:
    if hasattr(event, "delta"):
        print(event.delta, end="\n", flush=True)

