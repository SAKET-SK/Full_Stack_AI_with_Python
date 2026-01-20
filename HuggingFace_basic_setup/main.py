# HuggingFace basics - running the model locally

from transformers import pipeline

# pipeline = it means that we are running a model from the HuggingFace Hub
pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What is the capital of France?"},
            {"type": "image", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/1280px-Flag_of_France.svg.png"}
        ] 
    }
]

pipe(text=messages)
