# Building a Custom Tokenizer in Python using tiktoken
# This script demonstrates how to encode and decode text using the tiktoken library.

import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")  # Replace "gpt-4o" with your desired model name

text = "Hello, My name is Saket Khopkar."
tokens = encoder.encode(text)
print("Encoded Tokens:", tokens)

# For gpt-4o : Encoded Tokens: [13225, 11, 3673, 1308, 382, 54051, 292, 20724, 467, 10428, 13]

decoded_text = encoder.decode(tokens)
print("Decoded Text:", decoded_text)
