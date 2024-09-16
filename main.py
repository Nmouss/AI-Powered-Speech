# Nabil and Youssef 
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Function to write text to a file
def output_text(text):
    with open("output1.txt", "a") as f:
        f.write(text)
        f.write("\n")

# Function to continuously listen and process speech
def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(f"Recognized: {text}")

                # Output the recognized text to a file
                output_text(text)

                # Convert the recognized text to speech
                text_to_speech(text)

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio")

# Start the continuous listening
if __name__ == "__main__":
    record_text()
#Nabil is a poopoohead (Youssef is very unprofessional)
