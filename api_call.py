from google import genai
from dotenv import load_dotenv
import os
from io import BytesIO
from gtts import gTTS

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini API client
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = "gemini-3-flash-preview"

#note generation function
def generate_notes(image_urls):
    prompt = f"""Summarize the pictures in note format at max 200 words 
    and make sure add nassary markdown to diffrentiate diffrent sections {', '.join(image_urls)}"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        # config={
        #     "max_output_tokens": 500,
        #     "temperature": 0.7,
        # },
    )
    return response.text.strip()

#audio generation function
def generate_audio(text):
    speech = gTTS(text=text, lang='en', slow=False)
    audio_buffer = BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer.getvalue()

#quiz generation function
def generate_quiz(notes, difficulty):
    prompt = f"""Generate a 5  quizzes based on the following notes with 
    {difficulty} difficulty level and provide options for each question 
    with explanations and answers: {notes}"""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        # config={
        #     "max_output_tokens": 500,
        #     "temperature": 0.7,
        # },
    )
    return response.text.strip()
