import random
import time
import datetime

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "farewell": ["Goodbye!", "Bye!", "See you later!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "name": ["My name is Chatbot.", "I'm Chatbot!", "You can call me Chatbot."],
    "age": ["I'm just a computer program. I don't have an age.", "I don't age!"],
    "creator": ["I was created by a team of developers.", "My creator is a talented programmer."],
    "how_are_you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "where_from": ["I exist in the digital realm, so you can say I'm from the internet!",
              "I'm from the world wide web, here to assist you!"],
    "what_do_you_do": ["I'm here to assist you with any questions you have!", "I'm a chatbot designed to help you with various tasks."],
    "what_are_you_doing": ["I'm here, ready to help you!", "I'm currently assisting you with your inquiries."],
   "male_female": ["I don't have a gender as I'm just a computer program.", "I'm gender-neutral, as I'm a chatbot."],
     "okay": ["Okay!", "Got it!", "Sure thing!"],
    "time_of_day":{
        "morning": ["Good morning!", "Good to see you this morning!"],
        "afternoon": ["Good afternoon!", "Hope you're having a good afternoon!"],
        "evening": ["Good evening!", "Good to talk to you this evening!"]
    },
    "how_can_help": ["I can help you with a wide range of topics! Just ask me anything you'd like to know or need assistance with."],
     "happy_birthday": ["Happy Birthday! 🎉", "Wishing you a fantastic birthday! 🎂", "Happy Birthday! Have a wonderful day! 🎈"],
    "do_you_love_me": ["As an AI chatbot, I don't have feelings like humans do, but I'm here to assist you with anything you need!"],
    "current_date": [f"The current date is {datetime.date.today().strftime('%Y-%m-%d')}."],
    "current_time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."],
    "weather": ["I'm just a chatbot. I don't know the weather.", "You should check a weather website for that."],
    "default": ["Sorry, I don't understand.", "Can you please rephrase that?", "I'm not sure what you mean."],
}

def get_response(user_input):
    user_input = user_input.lower()


    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["farewell"])
    elif "thanks" in user_input or "thank you" in user_input:
        return random.choice(responses["thanks"])
    elif "your name" in user_input:
        return random.choice(responses["name"])
    elif "your age" in user_input:
        return random.choice(responses["age"])
    elif "who created you" in user_input or "your creator" in user_input:
        return random.choice(responses["creator"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "weather" in user_input:
        return random.choice(responses["weather"])
    elif "where are you from" in user_input:
        return random.choice(responses["where_from"])
    elif "what do you do" in user_input or "what do you do?" in user_input:
        return random.choice(responses["what_do_you_do"])
    elif "what are you doing" in user_input or "what are you doing?" in user_input:
        return random.choice(responses["what_are_you_doing"])
    elif "are you male" in user_input or "are you female" in user_input:
        return random.choice(responses["male_female"])
    elif "okay" in user_input:
        return random.choice(responses["okay"])
    elif any(greeting in user_input for greeting in ["good morning", "good morning!", "morning"]):
        return random.choice(responses["time_of_day"]["morning"])
    elif any(greeting in user_input for greeting in ["good afternoon", "good afternoon!", "afternoon"]):
        return random.choice(responses["time_of_day"]["afternoon"])
    elif any(greeting in user_input for greeting in ["good evening", "good evening!", "evening"]):
        return random.choice(responses["time_of_day"]["evening"])
    elif "how can you help me" in user_input or "how can you help me?" in user_input:
        return random.choice(responses["how_can_help"])
    elif "happy birthday" in user_input:
        return random.choice(responses["happy_birthday"])
    elif "do you love me" in user_input:
        return random.choice(responses["do_you_love_me"])
    elif "date" in user_input:
        return random.choice(responses["current_date"])
    elif "time" in user_input:
        return random.choice(responses["current_time"])
    else:
        return random.choice(responses["default"])


print("Hello! I am a basic chatbot. How can I assist you today?")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)


    if user_input.lower() == "bye":
        break
