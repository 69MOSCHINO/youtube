import openai
import random
import os

def generate_story_or_quote():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_type = random.choice(["motivazionale", "storiella divertente", "fiaba breve"])
    prompt = f"Scrivi una {prompt_type} in italiano, massimo 3 frasi."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response['choices'][0]['message']['content'].strip()
    return text, "storiella" in prompt_type or "fiaba" in prompt_type