import speech_recognition as sr
import asyncio
from openai import OpenAI
from dotenv import load_dotenv

from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="nova",
        instructions="Always speak in happy, joyful and delighful manner",
        input=speech,
        response_format="pcm"
    )as response:
        await LocalAudioPlayer().play(response)
        
def main():
    r = sr.Recognizer()    # This does the Speech to Text thing (STT)

    with sr.Microphone() as source:   # Takes Mic access
        r.adjust_for_ambient_noise(source)  # Cutting of the background noise
        r.pause_threshold = 2     # Time to wait for a phrase to start

        while True:
            print("Speak....>>  ")
            audio = r.listen(source)

            print("Processing your audio....")
            stt = r.recognize_google(audio)

            print("You Said : ", stt)

            SYSTEM_PROMPT = f"""
                You are an expert voice agent, you are given a transcipt of what the use has siad in 
                his voice.
                You need to output as you are an voice agent and whatever you speak will be converted back
                to audio using AI and will be played back to the user.
            """

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": stt}
                ]
            )

            print("AI Response: ", response.choices[0].message.content)
            asyncio.run(tts(response.choices[0].message.content))

main()
