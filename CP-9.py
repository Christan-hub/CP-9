# importing pyttsx3
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import datetime
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors


def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
    return Query

# creating Speak() function to giving Speaking power
# to our voice assistant


def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
     while True:
        command = take_commands()

        if "exit" in command:
            Speak("Sure sir! as your wish, bye Thank You")
            break

        if "hello" in command:
            Speak("Hello sir Good morning. How may I help you")
        
        if "how are you" in command:
            Speak("I am Fine sir. What About You...")
        
        if "YouTube" in command:
            Speak("sure sir")
            webbrowser.open("youtube.com")
        
        if "Google" in command:
            Speak("sure sir")
            webbrowser.open("google.com")
        
        if "name" in command:
            Speak(" sure sir. Your name is Christan Robert Pereira")
        
        if "call" in command:
            Speak(" You can call me CP-9!")
        
        if "language" in command:
            Speak("English, Marathi and Hindi. sir")

        if "Wikipedia" in command:
            Speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            Speak("According to wikipedia")
            print(results)
            Speak(results)

        elif "the time" in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"sir, the time is {strTime}")

        elif "open code" in command:
            Speak("Ok sir... opening code")
            codePath = "C:\\Users\\chris\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif "play music" in command:
            Speak("Ok sir")
            music_dir = 'C:\\Users\\Chris\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
