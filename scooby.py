import pyttsx3
import datetime
import speech_recognition as sr
  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr Kanwar")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon! Mr Kanwar ")
    
    elif hour>=16 and hour<20:
        speak("Good Evening! Mr Kanwar")

    else:
        speak("Good Night! Mr Kanwar")
    
    speak("I am Scooby, How may i assist you ?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print("user said: ",query)

    except Exception:
        #print(e)   
        print("Say that again....")
        return "None"
    
    return query



if __name__=="__main__":
    #speak("Divij Kanwar is my hero")
    wishMe()
    #takeCommand()