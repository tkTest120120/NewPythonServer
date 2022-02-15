from gtts import gTTS
import playsound

fileName = "../Public/sound.mp3"

def speak(text):
    # print("Trợ Lý ảo:  ", text)

    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # rate = engine.getProperty('rate')
    # volume = engine.getProperty('volume')
    # engine.setProperty('volume', volume - 0.0)  # tu 0.0 -> 1.0
    # engine.setProperty('rate', rate - 50)
    # engine.setProperty('voice', voices[1].id)
    # engine.say(text)
    # engine.runAndWait()


    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save(fileName)
    playsound.playsound("sound.mp3", True)
    # os.remove("sound.mp3")
    print("\n\nxong")

speak("xin chào tất cả mọi người")