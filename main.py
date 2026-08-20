import speech_recognition as sr
import subprocess as sp
import asyncio as asc
import edge_tts as edt


def speak(txt):
    print(txt)
    asc.run(say(txt))


VOICE="en-US-AvaNeural"
OUTPUT_FILE="output.mp3"

async def say(txt):
    communicate = edt.Communicate(txt,VOICE)
    await communicate.save(OUTPUT_FILE)
    sp.run(["mpg123","output.mp3"])

speak("hello pratyush")

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
                speak("I am running good")
            elif "this is cool" in text.lower():
                speak("I know right")
            elif text.lower()=="open terminal":
                sp.run(["kitty"])
            elif text.lower()=="open browser":
                sp.run(["firefox"])
            elif text.lower()=="open calculator":
                sp.Popen(["gnome-calculator"])
            elif text.lower()=="close calculator":
                sp.run(["pkill","gnome-calculato"])
            elif "add" in text.lower():
                t=text.lower().split(" ")
                total=0
                for i in t:
                    if i.isdigit():
                        total+=int(i)
                res=f"sum is {total}"
                speak(res)
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google service; {e}")
            break

speak("goodbye")
