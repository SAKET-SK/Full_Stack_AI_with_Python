from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()   

client = OpenAI(
    api_key="AIzaSyCqU1FqRq4vmrQUfiPDNXgN3RnqH03iTy4",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)      # Making a GET request to the URL

    if response.status_code == 200:
        return f"The weather in the {city} is {response.text}"
    
    return "Something went wrong. Please try again."

available_tools = {
    "get_weather": get_weather
}


def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",          
        messages=[
            {"role": "user", "content": user_query}     
        ]
    )
    print(response.choices[0].message.content)  

# print(get_weather("Pune"))   # Test with different cities
main()

