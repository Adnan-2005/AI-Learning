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
# 3 prompts to test the model
prompt1="what are Executors in java programming language?"
prompt2="what is the difference between Executor and ExecutorService?"
prompt3="how do you create a custom Executor in java?"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages , max_tokens=800)
    usage=response.usage
    print(f"Prompt: {prompt} ---> your_tokens: {usage.prompt_tokens}, completion_tokens: {usage.completion_tokens}, total_tokens: {usage.total_tokens} finish token: {response.choices[0].finish_reason}")
    # print(response)

    # print("#####################")

    # answer=response.choices[0].message.content
    # print(answer)

# message = {
#     "role": role,
#     "content": prompt
# }
# messages=[message]
# response=client.chat.completions.create(model=model, messages=messages)
# print(response)

# print("#####################")

# answer=response.choices[0].message.content
# print(answer)
