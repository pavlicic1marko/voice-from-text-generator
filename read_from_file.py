from gtts import gTTS
import os

text = open('demo.txt','r').read()

language = 'en'  # sr is for Serbian, en for English
audio_output = gTTS(text=text, lang=language, slow=False)
audio_output.save('audio_from_file.mp3')

os.system("start audio_from_file.mp3")

