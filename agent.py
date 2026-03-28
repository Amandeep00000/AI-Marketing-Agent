from openai import OpenAI
from prompts import marketing_prompt
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key="your_key")

def run_agent(user_input):
    prompt = marketing_prompt(user_input)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output[0].content[0].text