from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=GEMINI_API_KEY)

#note generation function
def generate_notes(image_urls):
    prompt = f"""Summarize the pictures in note format at max 200 words 
    and make sure add nassary markdown to diffrentiate diffrent sections {', '.join(image_urls)}"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        # config={
        #     "max_output_tokens": 500,
        #     "temperature": 0.7,
        # },
    )
    return response.text.strip()