import pyttsx3 as pt
import speech_recognition as sr
import subprocess as sp

engine = pt.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)  
engine.setProperty('volume', 1)  
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("hello pratyush.")
engine.runAndWait()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("adjusting amience wait..")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("microphone is live")

    text=""
    while(text!="please quit"):
        try:
            print("listening..")
            audioData=recognizer.listen(source)
            print("transcribing..")
            text=recognizer.recognize_google(audioData)
            print(f"u said: {text}")
            if "how are you" in text.lower():
                engine.say("I am running good")
                engine.runAndWait()
            elif "this is cool" in text.lower():
                engine.say("I know right")
                engine.runAndWait()
            elif text.lower()=="open terminal":
                sp.run(["kitty"])
            elif text.lower()=="open browser":
                sp.run(["firefox"])

        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google service; {e}")
            break

engine.say("goodbye")
engine.runAndWait()
