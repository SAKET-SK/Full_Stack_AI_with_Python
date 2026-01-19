Notes on Prompt Serialization and Types:

---------------------------------------------------------------------------------------------

1) Alpaca Prompting Template: Used by Alpaca Models and Meta LLAMA Models.

Example:
```
### Instructions: <SYSTEM PROMPT>\n
### Input: <USER QUERY>\n
### Response:      \n
```

Live Conversion Example:

Original Prompt

```python
response = client.chat.completions.create( 
    model="gemini-2.5-flash", 
    messages=[ 
        {"role": "system", "content": SYSTEM_PROMPT}, 
        {"role": "user", "content": "What is the recipe for Chicken 65?"} 
    ] 
)
```
Converted to Alpaca Prompting Template

```
### Instruction:
What is the recipe for Chicken 65?

### Input:
<SYSTEM_PROMPT content goes here, if you still want to keep system behavior>

### Response:

```

---------------------------------------------------------------------------------------------

2) ChatML : Used by OpenAI , Gemini

- Can be seen in code we did previously.
- Big Tech Giants use this; 99% of the time, we are bound to use this in our Gen AI journey.

Example:

```python
{
    "role": "system" | "user" | "assistant",
    "content": "string"
}
```

---------------------------------------------------------------------------------------------

3) INST Prompting : Used by LLAMA 2

Example:

```
[INST] <USER_QUERY> [/INST]
```

---------------------------------------------------------------------------------------------

This section is just a good to have knowledge type of section.
Go to ChatGPT and convert your prompts to these specific styles to get more understanding.

