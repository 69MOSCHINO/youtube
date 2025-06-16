from gtts import gTTS
import os

def generate_audio(text, filename='output_audio.mp3'):
    tts = gTTS(text=text, lang='it')
    tts.save(filename)
    return filename