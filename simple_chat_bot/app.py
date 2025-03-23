from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyttsx3

# Initialize the FastAPI app
app = FastAPI()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to make the assistant speak
def speak(text: str):
    engine.say(text)
    engine.runAndWait()

# Define the input model for user commands
class UserInput(BaseModel):
    command: str

@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Welcome to Mallareddy College Bot API!"}

@app.post("/talk")
def talk(user_input: UserInput):
    """
    Handle user commands and return bot responses.
    """
    command = user_input.command.lower()
    response = ""

    # Respond to commands
    if "hello" in command:
        response = "Hi there! Welcome to Mallareddy College."
    elif "what's your name" in command or "your name" in command or "name" in command:
        response = "My name is Simple Bot from Mallareddy College."
    elif "what are the branches available in this college" in command or "branches" in command:
        response = "Mallareddy College provides branches like AI/ML, CSE, IT, ECE, EEE, MECH, CIVIL."
    elif "what's the fee for CSE, IT, ECE, EEE, MECH, CIVIL" in command or "fee" in command:
        response = "The fee for CSE, IT, ECE, EEE, MECH, CIVIL is 1,00,000."
    elif "where is the Mallareddy College located" in command or "location" in command:
        response = "Mallareddy College is located in Maisammaguda, Dhulapally, Secunderabad, Telangana 500100."
    elif "goodbye" in command:
        response = "Goodbye! Have a great day at Mallareddy College."
    else:
        response = "I didn't understand that. Please try again."

    # Speak the response
    speak(response)
    return {"response": response}
