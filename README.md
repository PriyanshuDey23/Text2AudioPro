
# Text2Audio

A versatile text-to-speech application that allows users to upload text through PDF, URL, or direct input. It uses the Gemini AI model for optional summarization and converts text to audio for playback or download. This application leverages advanced technologies such as Google Gemini and gTTS to provide seamless text-to-speech capabilities.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Tech Stack](#tech-stack)
- [License](#license)

---

## Overview
The **Text2Audio** application provides an easy-to-use platform for converting text into speech, with additional options for summarizing the content using the Gemini AI model. Users can upload text via PDFs, URLs, or directly enter text to generate spoken audio, which can be downloaded for offline use.

---

## Features
- **Text Input Options**: Upload a PDF, enter a URL, or type text directly.
- **Summarization**: Option to generate a summary using the Gemini AI model.
- **Text-to-Speech (t2s)**: Convert the input text or summary to audio using Google Text-to-Speech (gTTS).
- **Streamlit UI**: Simple and interactive interface for user-friendly experience.
- **Audio Playback and Download**: Stream and download the generated audio file.
- **Customizable Prompts**: Tailor the summarization or text processing with customizable prompts.

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/PriyanshuDey23/Text2AudioPro.git
```

### Step 2: Set up a Virtual Environment
Set up a virtual environment to manage the project's dependencies:
```bash
conda create -n text2audio python=3.10 -y
conda activate text2audio
```

### Step 3: Install Dependencies
Install all required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 4: Configure API Keys
Create a `.env` file in the root directory to store your API credentials:
```ini
GOOGLE_API_KEY="your_google_api_key"
```

### Step 5: Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```

Access the application in your browser at:
```bash
http://localhost:8501
```

---

## Tech Stack
- **Python**: The core programming language used in the application.
- **Google Gemini API**: For natural language processing and summarization.
- **gTTS (Google Text-to-Speech)**: Converts text into audio.
- **Streamlit**: Framework for creating the user interface.
- **dotenv**: Used for managing environment variables, such as the Google API key.
- **pymupdf**: To extract text from PDF files (used in `extract_text_from_pdf` function).
- **beautifulsoup4**: For fetching content from URLs (used in `extract_text_from_url` function).

---

## License
This project is licensed under the [MIT License](LICENSE).

---

### Contributing
We welcome contributions to improve the **Text2Audio** application! Feel free to fork the repository and submit pull requests. For significant changes, please open an issue first to discuss your proposed modifications.


