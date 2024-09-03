import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Original: {text}")
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None
