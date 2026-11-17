import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError('GEMINI_API_KEY não encontrada')

client = genai.Client(api_key=api_key)

def generate_response(client, user_massage: str) -> str:
# receber a mensage
    client.models = 'gemini-3.8-flash'
    user_massage = 
# enviar ela para o Gemini
    response = client.models, user_massage
# retornar o texto gerado  reponse.text
    return response.text