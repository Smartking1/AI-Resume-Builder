# groq_client.py

from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model_name = MODEL_NAME

    def generate_text(self, prompt):
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model_name,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error during text generation: {e}")
            return None