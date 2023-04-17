from dotenv import load_dotenv
import openai
import os

load_dotenv()

discord_token = os.getenv('OPENAI_API_KEY')

def chatgpt_response(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=500
  )
  prompt_response = ""
  response_dict = response.get("choices")
  if response_dict and len(response_dict) > 0:
    prompt_response = response_dict[0]["text"]
  return prompt_response
  