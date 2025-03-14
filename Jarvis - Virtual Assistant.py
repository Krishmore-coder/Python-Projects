import speech_recognition as sr
import pyttsx3
import webbrowser
import random
musics = {
    "tenu le":"https://www.youtube.com/watch?v=fi7QcFrPCx0&list=RDfi7QcFrPCx0&start_radio=1",
    "russian bhadana":"https://www.youtube.com/watch?v=1OAjeECW90E&list=RDMMfi7QcFrPCx0&index=3",
    "triple o g":"https://www.youtube.com/watch?v=pqZuSz8_2DM&list=RDMMfi7QcFrPCx0&index=2",
    "triple o ji":"https://www.youtube.com/watch?v=pqZuSz8_2DM&list=RDMMfi7QcFrPCx0&index=2",
    "triple og":"https://www.youtube.com/watch?v=pqZuSz8_2DM&list=RDMMfi7QcFrPCx0&index=2",
}
recognizer = sr.Recognizer()
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()
speak("Initializing jarvis")
while True:
    try:
        with sr.Microphone() as source:
            print("Listening.......")
            recognizer.adjust_for_ambient_noise(source=source)
            word = recognizer.listen(source=source,timeout=5,phrase_time_limit=10) #timeout=Maximum time to wait for the user to start speaking. And phase_time_limit=Maximum time to record speech after speaking starts.
            word = recognizer.recognize_google(word)
        if "jarvis"==word.lower():
            speak("Yes sir")
            with sr.Microphone() as source:
                print("Jarvis Activated")
                recognizer.adjust_for_ambient_noise(source=source)
                audio = recognizer.listen(source=source,timeout=5,phrase_time_limit=10) #timeout=Maximum time to wait for the user to start speaking. And phase_time_limit=Maximum time to record speech after speaking starts.  
                audio = recognizer.recognize_google(audio)
                print(audio.lower())
            if audio.lower().startswith("open "):
                audio = audio.lower().replace("open ","")
                speak(f"opening {audio}")
                webbrowser.open(f"www.{audio}.com")
            elif "how are you jarvis"==audio.lower() or "jarvis how are you"==audio.lower() or "how are you"==audio.lower() or "how r u"==audio.lower():
                responses = ["I'm just a virtual assistant, but I'm feeling great! How about you?","I'm doing fantastic! Thanks for asking. Ready to assist you with anything!","I'm functioning at optimal capacity. How can I assist you today?","I'm great—no bugs today! Hopefully, it stays that way.","I'm good! Thanks for asking. What can I do for you?"]
                r = random.choice([0,1,2,3,4])
                speak(responses[r])
            elif audio.lower().startswith("play "):
                if audio.lower().endswith("music"):
                    audio = audio.lower().replace("play ","").replace(" music","")
                elif audio.lower().endswith("song"):
                    audio = audio.lower().replace("play ","").replace(" song","")
                else:
                    audio = audio.lower().replace("play ","")
                webbrowser.open(musics.get(audio.lower()))
            elif "thank you" in audio.lower() or "thankyou" in audio.lower() or "thank u" in audio.lower() or "thank" in audio.lower():
                speak("Your welcome sir!")
            elif "who are you"==audio.lower() or "who r u"==audio.lower() or "hu r u"==audio.lower():
                response = ["I'm your personal virtual assistant, here to help with anything you need!","I'm an A I powered assistant, ready to make your life easier!","I'm a digital assistant designed to provide information, answer questions, and assist you in any way I can!","I'm your friendly AI assistant! What can I do for you today?"]
                r = random.choice([0,1,2,3])
                speak(response[r])
    except Exception as e:
        print(f"Error: {e}")
