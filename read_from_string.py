from gtts import gTTS
import os

text = "LOL say something about chat gpt"
audio_output = gTTS(text=text, lang='en', slow=False)  # slow is the speed of speach
audio_output.save('audio.mp3')

#start command is for windows os to play the amp3 file, for mac is afplay
os.system("start audio.mp3")
