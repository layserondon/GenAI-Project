from app.services.llm_service import generate_response
from app.core.agent_instruction import AGENT_INSTRUCTIONS

response = generate_response(
    'Explique três características harmônicas comuns no Neo Soul ' \
    'e como posso explorá-las em uma composição original.'
)

print(response)

