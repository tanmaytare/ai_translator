from speech_recognition_module import recognize_speech
from translation import translate_text
from text_to_speech import text_to_speech
from ui import start_ui

def translate_speech():
    original_text = recognize_speech()
    if original_text:
        translated_text = translate_text(original_text)
        text_to_speech(translated_text)
        return original_text, translated_text
    return None, None

if __name__ == "__main__":
    start_ui(translate_speech)
