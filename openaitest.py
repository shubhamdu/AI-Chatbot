import os
import google.generativeai as genai
from config import apikey  # config.py se apikey import kar rahe hain

# API key ko configure karna
genai.configure(api_key=apikey)

# Model Configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "write a email\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Please tell me what you want the email to say! I need information like:\n\n* **Who is the recipient?** (e.g., a friend, a professor, a potential employer)\n* **What is the purpose of the email?** (e.g., to request information, to schedule a meeting, to make a complaint, to follow up on a previous conversation)\n* **What information needs to be included?** (e.g., dates, times, names, addresses, specific questions)\n* **What is the desired tone?** (e.g., formal, informal, friendly, professional)\n\nOnce I have this information, I can write a suitable email for you.\n",
            ],
        },
    ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)