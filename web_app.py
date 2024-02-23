from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os

app = Flask(__name__, template_folder="templates")


def create_audio(text):
    text = text
    audio_output = gTTS(text=text, lang='en', slow=False)  # slow is the speed of speach
    audio_output.save('audio.mp3')


def play_audio():
    os.system("start audio.mp3")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    print("this is a test")
    text = request.form['text']
    create_audio(text)
    play_audio()
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
