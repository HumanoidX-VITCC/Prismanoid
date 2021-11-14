# Importing all the necessary libraries
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import requests


print('Loading your personal humanoid - Prisma')

# Initiate the voice engine using pyttsx3
engine=pyttsx3.init() 

'''engine=pyttsx3.init()
   - For MAC and Linux, as 'sapi5' is the default voice engine for Microsoft windows.
   - For linux, you also need to install libespeak using-
     sudo apt-get install libespeak (Example for Debian distros)
'''

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # 0 for male, 1 for female


def speak(text):
    '''Speaks the string given as the parameter'''
    engine.say(text)
    engine.runAndWait()

def wishMe():
    '''greetings based on the time of the day'''
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

        
def takeCommand():
    '''Defines the input (microphone)'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in') # Convert speech to text
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your personal humanoid Prisma")
wishMe()

# Main program
if __name__=='__main__':

    # Loop to keep the assistant on
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower() # Take command
        if statement==0:
            continue 

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal humanoid Prisma is shutting down, Good bye')
            print('your personal humanoid is shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"] - 273
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature is " +
                      str(current_temperature) + " degrees celsius" +
                      "\n The humidity is " +
                      str(current_humidity) + " percentage"
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in celsius unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Prisma version 1, your persoanl humanoid. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and much much more!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by HumanoidX")
            print("I was built by HumanoidX")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

time.sleep(3)