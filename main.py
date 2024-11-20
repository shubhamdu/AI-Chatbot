import datetime
import speech_recognition as sr
import os
import webbrowser
import pyjokes
import openai
import google.generativeai as genai
from config import apikey

# Configure API keys
genai.configure(api_key=apikey)

chatStr = ""
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

def chat(query):
    """Chat using Gemini API."""
    global chatStr
    print(chatStr)
    chatStr += f"Shubham: {query}\n Shivam: "

    try:
        # Generate response using the correct method
        response = genai.generate(
            prompt=chatStr,                 # Pass the chat history as the prompt
            **generation_config             # Use the generation config
        )

        # Extract response text
        reply = response.generations[0].text  # Fetch the first generation's text
        say(reply)
        chatStr += f"{reply}\n"
        return reply

    except Exception as e:
        print(f"Error in Gemini API: {e}")
        return "Sorry, I couldn't process that."

def say(text):
    """Function to convert text to speech."""
    try:
        if os.name == 'nt':  # For Windows
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        else:  # For macOS or Linux
            os.system(f"say {text}")
    except Exception as e:
        print(f"Error in text-to-speech: {e}")


def take_command():
    """Function to take voice commands from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            message = "Could not understand your voice. Please try again."
            say(message)
            print(message)
            return ""
        except sr.RequestError:
            message = "Speech service is unavailable. Check your internet connection."
            say(message)
            print(message)
            return ""


def open_website(query, sites):
    """Function to open websites based on the user's query."""
    for site in sites:
        if f"open {site[0].lower()}" in query.lower():
            say(f"Opening {site[0]}...")
            webbrowser.open(site[1])
            return True
    return False


def tell_time():
    """Function to tell the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M")
    say(f"The current time is {current_time}")
    print(f"The current time is {current_time}")


def tell_joke():
    """Function to tell a joke."""
    joke = pyjokes.get_joke()
    say(joke)
    print(joke)


def generate_email():
    """Function to generate email using generative AI."""
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "write a formal email to a professor regarding project progress.",
                ],
            },
        ]
    )

    # Input message details for the email
    input_details = (
        "I am writing to Professor to request a meeting regarding the project progress. "
        "I am available on Monday and Wednesday afternoons. "
        "The tone should be formal."
    )

    response = chat_session.send_message(input_details)
    say("Here is the email content that I have generated.")
    print(response.text)
    return response.text


if __name__ == "__main__":
    say("Hello, I am Alexa. How can I help you?")
    sites = [
        ["YouTube", "https://youtube.com"],
        ["Twitter", "https://x.com"],
        ["Google", "https://google.com"]
    ]

    while True:
        query = take_command()

        if query:
            # Handle website opening
            if open_website(query, sites):
                continue

        if "time" in query.lower():
            tell_time()
            continue

        if "joke" in query.lower():
            tell_joke()
            continue

        if "email" in query.lower():
            email_content = generate_email()
            print("Generated Email Content:")
            print(email_content)
            continue

        # Exit the program
        if "exit" in query.lower() or "quit" in query.lower():
            say("Goodbye! Have a nice day.")
            break

        else:
            print("Chatting...")
            chat(query)