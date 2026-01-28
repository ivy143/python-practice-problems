# Implement a simple chatbot
def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "what is your name?": "I'm a simple chatbot created to assist you.",
        "bye": "Goodbye! Have a great day!"
    }
    
    # Normalize user input to lowercase
    user_input = user_input.lower()
    
    # Return the corresponding response or a default message
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you ask something else?")
# Example usage
print(chatbot_response("Hi"))  # Output: Hello! How can I help you today?
print(chatbot_response("What is your name?"))  # Output: I'm a simple chatbot created to assist you.
print(chatbot_response("Tell me a joke"))  # Output: I'm sorry, I don't understand that. Can you asksomething else?
print(chatbot_response("bye"))  # Output: Goodbye! Have a great day!
# Example usage
print(chatbot_response("Hi"))  # Output: Hello! How can I help you today?
print(chatbot_response("What is your name?"))  # Output: I'm a simple chatbot created to assist you.
print(chatbot_response("Tell me a joke"))  # Output: I'm sorry, I don't understand that. Can you ask something else?
print(chatbot_response("bye"))  # Output: Goodbye! Have a great day!
import speech_recognition as sr
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""
# Example usage with voice interaction
user_input = listen()
response = chatbot_response(user_input)
print(response)
speak(response)
