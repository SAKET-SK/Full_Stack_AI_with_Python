# Since OpenAI keys are paid, Gemini keys are free to use ***for now***.
# So a good free alternative to OpenAI is Gemini by Google.
# Below is an example of how to use Gemini API in Python.

# pip install google-genai

from google import genai

client = genai.Client(
    api_key='GEMINI_API_KEY'   # Replace with your Gemini API key   
)   # creates a client, which we can utilize to call Gemini APIs

response = client.models.generate_content(
    model = "gemini-2.5-flash", 
    contents = "Explain me the theory of relativity in simple terms."
)

print(response.text)   # This will print the response from Gemini
