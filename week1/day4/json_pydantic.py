import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

## structured it
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    contact_number: str
    address: str
    issue: str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_format=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

message_system = {
    "role": "system",   
    "content": system_format
}
text="hello My name is  Adnan . I have a iphone which is not working at all . My address is Jaunpur . My email is addy@example.com . My contact number is 912967" 
prompt=f"""
This is a customer ticket please extract personal information from this
{text}
"""
message = {
    "role": role,
    "content": prompt
}
messages=[message_system, message]
response=client.chat.completions.create(model=model, messages=messages , response_format=response_format)


answer=response.choices[0].message.content
print(answer)


## isko padhte kaise hai

import json
data_file=json.loads(answer)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.contact_number)
print(ticket.address)
print(ticket.issue)
