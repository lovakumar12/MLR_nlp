from flask import Flask, render_template, request
import pyttsx3
import threading
import queue
import time

app = Flask(__name__)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
engine_queue = queue.Queue()

def engine_worker():
    """Thread worker to process TTS commands from the queue."""
    while True:
        text = engine_queue.get()  # Wait for new text to speak
        if text is None:  # Exit condition for the worker thread
            break
        engine.say(text)
        engine.runAndWait()
        engine_queue.task_done()

# Start the worker thread
threading.Thread(target=engine_worker, daemon=True).start()

def speak(text):
    """Add text to the queue for speaking and debug output."""
    print(f"[DEBUG] Adding to speak queue: {text}")
    engine_queue.put(text)

def process_command(command):
    """Process user commands and return bot responses."""
    if "hello" in command:
        response = "Hi there! Welcome to Mallareddy College."
    elif "what's your name" in command or "your name" in command or "name" in command:
        response = "My name is Simple Bot from Mallareddy College."
    elif "what are the branches available in this college" in command or "branches" in command:
        response = "Mallareddy College provides branches like AI/ML, CSE, IT, ECE, EEE, MECH, and CIVIL."
    elif "what's the fee" in command or "fee" in command:
        response = "The fee for CSE, IT, ECE, EEE, MECH, and CIVIL is 1,00,000."
    elif "where is the Mallareddy College located" in command or "location" in command:
        response = "Mallareddy College is located in Maisammaguda, Dhulapally, Secunderabad, Telangana 500100."
    elif "goodbye" in command:
        response = "Goodbye! Have a great day at Mallareddy College."
    else:
        response = "I didn't understand that. Please try again."
    
    # Speak the response
    speak(response)
    return response

@app.route("/", methods=["GET", "POST"])
def home():
    bot_response = ""
    if request.method == "POST":
        user_command = request.form.get("user_input", "").lower()
        bot_response = process_command(user_command)
    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    try:
        print("[DEBUG] Starting Flask app...")
        app.run(debug=True)
    finally:
        print("[DEBUG] Shutting down worker thread...")
        engine_queue.put(None)
        engine_queue.join()
