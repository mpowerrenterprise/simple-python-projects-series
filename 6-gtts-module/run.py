import gtts
import playsound


audio = gtts.gTTS(text="Hello, This is a simple python program", lang='en', slow=False)
audio.save("output.mp3")

playsound.playsound("output.mp3")