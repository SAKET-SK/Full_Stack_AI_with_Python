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
        # This sets the behavior of the assistant in the conversation i.e. PROMPTING BASICS
        {"role": "system", "content": "You are a helpful assistant, always who always provides a philosophical thought before your answer."},    
        {"role": "user", "content": "Explain me black hole in 3 sentences."}     
    ]
)

print(response.choices[0].message.content)   

# Output of this program:
# The concept of a black hole, an ultimate compression of matter into a singularity, challenges our very notions of existence and non-existence, revealing that even the void can possess an overwhelming presence.

# A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it. This immense gravitational pull results from a vast amount of matter being squeezed into an incredibly small space, often the remnant of a massive star's collapse. The "event horizon" marks the point of no return, beyond which everything, including information, is drawn inexorably towards the singularity at its heart.
