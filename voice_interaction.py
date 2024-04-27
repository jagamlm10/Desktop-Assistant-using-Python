import speech_recognition as sr
import win32com.client


# Takes in text input and produces an automated voice that reads that text
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


# Takes in voice audio as input whenever the function is called and transcribes voice to text
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            print(f'User said:{query}')
            return query
        except Exception as e:
            return "Sorry, I misheard you, can you please repeat?"


if __name__ == '__main__':
    say("Try to say something")
    for i in range(5):
        print("Listening...")
        user_input = take_command()
        say(user_input)
