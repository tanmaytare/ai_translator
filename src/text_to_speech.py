from gtts import gTTS
import pygame
import os
from datetime import datetime

def text_to_speech(text, language='mr'):
    tts = gTTS(text, lang=language)
    filename = f"translated_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(filename)
