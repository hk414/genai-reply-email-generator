# Email Reply Generator with Groq API

This project provides an email reply generator using the **Groq API**. The tool takes an original email and an optional additional reply content, then generates a professional, polite, and contextually appropriate email reply. If a resume is uploaded, the tool can include relevant details from the resume in the reply. 

## Features
- Generate email replies based on the provided original email.
- Optionally upload a resume, with the tool extracting relevant details and mentioning the resume in the reply.
- Provides only the body of the generated reply email, without any extra metadata.

## Requirements

- Python 3.10 or higher
- **Groq API key** (see below for instructions)
- Streamlit (for the web interface)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hk414/genai-reply-email-generator.git
cd email-reply-generator
```

### 2. Set Up Profile
Create a profile.txt and include relevant information.

### 3. Set Up Your Environmmet
```bash
pip install -r requirements.txt
```

### 4. Configure Your Groq API Key
You will need a Groq API key to use the email generation service. Follow these steps to configure it:

Create a .env file in the project root directory.

```bash
GROQ_API_KEY=your_api_key_here
```

### 5. Run the app
```bash
streamlit run main.py 
```