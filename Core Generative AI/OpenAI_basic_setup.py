from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # loads the .env file and sets the environment variables, very important step!! 
# You should have the environment variable set by the name : OPENAI_API_KEY in your .env file.

# Example content of .env

# OPENAI_API_KEY=your_openai_api_key_here

client = OpenAI()   # creates a client, which we can utilize to call OpenAI APIs

response = client.chat.completions.create(
    model="gpt-3.5-turbo",        # Any model of your choice can be used here   
    messages=[
        {"role": "user", "content": "Hello, My name is Saket Khopkar."}     # This is how you pass the data to your GPT
    ]
)

print(response.choices[0].message.content)   # This will print the response from GPT
