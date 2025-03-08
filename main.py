import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")

client = Groq(api_key=GROK_API_KEY)

def load_profile():
    try:
        with open("profile.txt", "r") as file:
            profile_info = file.read().strip()  
        return profile_info
    except FileNotFoundError:
        return "Profile information not found."

profile = load_profile()

def generate_reply_email(original_email, reply_content, include_resume=False, resume=None):
    system_message = f"""
    You are a helpful assistant that helps to write professional emails. 
    
    {profile} 
    
    Instructions: 
    1. Read the original email carefully.
    2. Write a professional, polite, and contextually appropriate reply based on the original email's content.
    3. If the user has provided additional reply content, include it in the response.
    4. If a resume is included, extract relevant information from the resume (if possible) and reference it in the reply.
    5. Only provide the reply email body (no additional information).
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": f"Original email: \n{original_email}\n\nReply: {reply_content}",
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    
    generated_reply = chat_completion.choices[0].message.content.strip()

    if include_resume and resume is not None:
        generated_reply += f"\n\nAttached: {resume.name}"

    return generated_reply

def main():
    st.title("Email Reply Generator")

    st.header("Original Email Details")
    original_email = st.text_area("Original Email Body", "")

    st.header("Your Reply")
    reply_content = st.text_area("Reply Content", "")

    include_resume = st.checkbox("Include Resume in Reply?", value=False)
    
    resume = None
    if include_resume:
        resume = st.file_uploader("Upload Resume (Optional)", type=["pdf", "docx", "txt"])

    if st.button("Generate Reply Email"):
        generated_reply = generate_reply_email(original_email, reply_content, include_resume, resume)

        st.subheader("Generated Reply Email")
        st.write(generated_reply)

if __name__ == "__main__":
    main()
