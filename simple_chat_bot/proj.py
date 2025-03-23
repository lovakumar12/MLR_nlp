

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def main():
    # Welcome message
    speak("Hello! I am your simple bot from Mallareddy College.")
    speak("You can say hello, ask my name, or say goodbye.")

    while True:
        # Get user input
        command = input("You: ").lower()
        
        # Respond to commands
        if "hello" in command:
            speak("Hi there! Welcome to Mallareddy College.")
        elif "what's your name" in command or "your name" in command or "name" in command:
            speak("My name is Simple Bot from Mallareddy College.")
        elif "what are the branches available in this college" in command  or "branches" in command :
            speak("Mallareddy College.provides branches like AI/ML , CSE,IT,ECE,EEE,MECH,CIVIL")
        elif "what's the fee for CSE,IT,ECE,EEE,MECH,CIVI" in command  or "fee" in command :
            speak("The fee for CSE,IT,ECE,EEE,MECH,CIVIL is 1,00,000")
        elif "where is the Mallareddy College located " in command or "location" in command:
            speak("Mallareddy College is located in Maisammaguda, Dhulapally, Secunderabad, Telangana 500100")
            
        elif "goodbye" in command:
            speak("Goodbye! Have a great day at Mallareddy College.")
            break
        else:
            speak("I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
