# Using Google Gemini with OpenAI Compatible API
# Most of the time, we utilize the OpenAI API for various LLM tasks.
# However, since Google Gemini also provides a free alternative, many people are bound to use it.

# The writing style of Gemini API is very similar to OpenAI API. But in the end, a bit different.

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# The calls will be made to Google's Gemini API but using OpenAI's client structure.

response = client.chat.completions.create(
    model="gemini-2.5-flash",          
    messages=[
        {"role": "user", "content": "Hello, My name is Saket Khopkar."}     
    ]
)

print(response.choices[0].message.content)   
