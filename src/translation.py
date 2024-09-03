from deep_translator import GoogleTranslator

def translate_text(text, target_language='mr'):
    translator = GoogleTranslator(source='auto', target=target_language)
    translated = translator.translate(text)
    print(f"Translated: {translated}")
    return translated
