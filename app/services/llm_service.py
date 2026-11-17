import  os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from app.core.agent_instruction import AGENT_INSTRUCTIONS


load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError('GEMINI_API_KEY não encontrada')

client = genai.Client(api_key=api_key)

MODEL_NAME = 'gemini-3.8-flash' 

def generate_response(user_message: str) -> str:

    config = types.GenerateContentConfig(
        system_instruction=AGENT_INSTRUCTIONS
    )

    response = client.models.generate_content(
        model = MODEL_NAME,
        contents = user_message,
        config = config
    )
    return response.text