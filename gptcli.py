import credentials
import os 
import openai

notice = "This comand will only run once and has no memory"
print(notice)
question = input("What would you like to do with ChatGPT on the command line? \n")

# openai.organization= "org-dZC83VlU2rPYIZB6kOPCGLp4"
openai.organization=credentials.organization
openai.api_key=credentials.OPENAI_API_KEY

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role" : "system", "content" : "Your are to help linux users remember command lines, answer with only the command that they need unless you are not sure how to help them."},
        {"role" : "user", "content" : "How do copy and paste in linux?"},
        {"role" : "system", "content" : "cp"},
        {"role" : "user", "content" : f"{question}"},
    ],
    temperature=0.3,

)
response

print(response['choices'][0]['message']['content'])
