from music_player import *
from voice_interaction import *
import webbrowser
import wikipedia
import datetime


# A function that checks whether the user has asked to open a website and if asked website is present then opens it
def check_websites(request):
    sites = [
        ["youtube", "http://youtube.com"],
        ["google", "http://google.com"],
        ["twitter", "https://twitter.com/"]
    ]
    for site in sites:
        if site[0].lower() in request.lower():
            say(f"Opening {site[0]}")
            webbrowser.open(site[1])
            return True
    return False


# A function to play music if user asks for it

'''
# todo:
-> Improve music selection process
-> Stop making it repeat for a new song everytime
-> Add feature to play a random music
'''


def play_music(query):
    if "play music" in query:
        say("Here is the list of available songs, please select the serial number...")
        available_songs()
        tune = take_command()
        print(f"User said : {tune}")
        try:
            play_song(tune)
        except Exception as e:
            say("Sorry, there were some problems...")
        return True
    return False


'''
# todo
-> Improve services
'''


def wiki(content):
    if "search for" in content:
        try:
            content = content.replace("search for", " ")
            results = wikipedia.summary(content, sentences=3)
            say("According to wikipedia...")
            print(results)
            say(results)
        except Exception as e:
            say("No information of this is available on wikipedia")
        return True
    return False


# What the bot can do
def skill(demand):
    if "can you do" in demand.lower():
        say("I can open some popular websites and play music....")
        say("I can search for some content on wikipedia...")
        say("I can also perform management tasks like telling the time, etcetera")
        return True
    return False


# A function for the bot to introduce itself
def intro():
    say("Hello I am Raphael sensei...")
    say("what would you like me to do for you...")


# Function to give the current time
def current_time(query):
    if "time" in query.lower():
        time = datetime.datetime.now().strftime("%H:%M")
        say(f'The time is {time}')
        return True
    return False


# A function to end the program when user mentions the keyword 'dismis'
def end(query):
    if "dismis" in query.lower():
        say("Thank you sir...")
        return True
    return False


if __name__ == '__main__':
    intro()
    # Continuously taking in user input and processing it
    while True:
        print("Listening...")
        query = take_command()
        # If user calls to end the program
        if end(query.lower()):
            break

        if skill(query.lower()):
            continue

        if current_time(query.lower()):
            continue

        # If user asks to play music
        if play_music(query.lower()):
            continue

        # If user demands to open a website
        if check_websites(query.lower()):
            continue

        # If user wishes to search for some content
        if wiki(query.lower()):
            continue
