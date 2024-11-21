Alexa - AI Virtual Assistant

This project is a Python-based AI Virtual Assistant named Alexa, designed to provide a variety of functionalities including chatting, opening websites, telling jokes, reporting the current time, generating emails, and more.

Features:
1. Voice Interaction: Alexa can recognize your voice commands and respond accordingly using speech synthesis.
2. Chatting: You can have a conversation with Alexa using the Gemini API.
3. Website Access: Open popular websites like YouTube, Google, and Twitter with voice commands.
4. Time Reporting: Ask Alexa for the current time, and it will provide the answer.
5. Joke Telling: Get a random joke for a bit of fun and laughter.
6. Email Generation: Generate email content using the Gemini API by providing a simple description.
7. Music Playback: Play pre-defined music stored on your device.
8. Extensible Design: Easily add more features, websites, or functionalities to the assistant.
   
Tech Stack:

Python Libraries:

1. speech_recognition - To recognize and process voice commands.
2. pyttsx3 - For text-to-speech functionality.
3. pyjokes - For generating jokes.
4. datetime - To fetch the current time.
5. webbrowser - To open websites.
6. openai - Used for AI-powered functionalities.
7. google.generativeai - Integrated for generative AI capabilities.
API: Google Gemini API (requires an API key).

Setup and Installation:

Prerequisites:
1. Python 3.8 or higher.
2. API Key for Google Gemini (place in a file named config.py as apikey = "your-api-key").
   
Installation
1. Clone the repository:
git clone [https://github.com/your-username/alexa-ai-assistant.git](https://github.com/shubhamdu/AI-Chatbot)
2. Navigate to the project directory:
cd alexa-ai-assistant
3. Install required dependencies:
pip install -r requirements.txt
4. Add your Gemini API key in config.py:
apikey = "your-api-key"

Usage
1. Run the program:
python main.py

2.Speak commands such as:
"Open YouTube."
"What time is it?"
"Tell me a joke."
"Generate an email to schedule a meeting."

3. Exit the assistant:
Say "exit" or "quit."

Project Structure:

1. main.py               # Main script for running Alexa
2. config.py             # API key storage
3. README.md             # Project documentation
4. requirements.txt      # Python dependencies
5. LICENSE               # License information (if any)
   
Commands List :

"Open <website>" = Opens popular websites (YouTube, Google).
"Time" = Reports the current time.
"Joke" = Tells a random joke.
"Email <content>"	= Generates an email based on input.
"Open Music" = Plays a pre-defined music file.
"Exit" or "Quit" = Exits the assistant.

Contributing:
Contributions are welcome! Feel free to fork the repository and submit a pull request.

License:
This project is licensed under the MIT License. See the LICENSE file for more details.

Author:
Shubham Chaurasia
B.Voc in Software Development, Delhi University
GitHub: shubhamdu
