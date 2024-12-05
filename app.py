import streamlit as st
from Text_To_Audio.helper import llm_model, text_to_speech
from Text_To_Audio.utils import extract_text_from_pdf, extract_text_from_url

# Function for handling various input types
def get_input_data():
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    url = st.text_input("Enter a URL")
    text = st.text_area("Enter your text", height=200)

    # Handle PDF input
    if uploaded_file:
        extracted_text = extract_text_from_pdf(uploaded_file)
        input_type = "PDF"
    # Handle URL input
    elif url:
        extracted_text = extract_text_from_url(url)
        input_type = "URL"
    # Handle direct text input
    elif text:
        extracted_text = text
        input_type = "Text"
    else:
        extracted_text = None
        input_type = None

    return extracted_text, input_type


# Streamlit App UI
st.set_page_config(page_title="Text2Audio")
st.header("Text2Audio")

# Get user input (file, URL, or direct text)
user_input, input_type = get_input_data()

# Display extracted or entered text
if user_input:
    st.text_area(f"Extracted Text from {input_type}", user_input, height=200)

# Provide options to the user for summarization or direct speech conversion
action = st.radio(
    "What would you like to do with the text?",
    ("Summarize and Convert to Audio", "Convert to Audio Only")
)

# Audio generation
if st.button("Generate Audio"):
    with st.spinner("Processing..."):
        if action == "Summarize and Convert to Audio":
            # Get LLM response based on the input text (summarization)
            response = llm_model(user_input)
        else:
            # Use the user input as is for direct text-to-speech conversion
            response = user_input

        # Convert the response (or original text) to audio
        audio_file_path = text_to_speech(response)

        # Read the generated audio file
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()

        # Display the response and provide audio playback/download
        st.text_area(label="LLM Response:", value=response, height=350)
        st.audio(audio_bytes)
        st.download_button(
            label="Download Speech",
            data=audio_bytes,
            file_name="speech.mp3",
            mime="audio/mp3"
        )
else:
    st.info("Please upload a PDF, enter a URL, or type some text to get started.")
