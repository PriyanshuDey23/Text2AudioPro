import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

# Load environment variables
load_dotenv()

# Configure the Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to convert text to speech and save it as an MP3 file
def text_to_speech(text, output_file="speech.mp3"):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(output_file)
        return output_file
    except Exception as e:
        raise ValueError(f"Error in text-to-speech conversion: {e}")

# Function to get a response from the Gemini model based on extracted text
def llm_model(user_input):
    try:
        # Initialize the model
        model = genai.GenerativeModel("gemini-1.5-flash-8b")
        
        # Construct a dynamic prompt based on the user input
        prompt = (
            "Please analyze the following text, extract the key points, and provide a "
            "clear and concise summary. Ensure the summary is accurate, formal, and "
            "reflects the essence of the original content. Here is the text:\n\n"
            f"{user_input}"
        )
        
        # Request response from the model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise ValueError(f"Error generating response from LLM: {e}")
