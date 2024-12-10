import random
from pyfiglet import figlet_format

def joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "There are 10 types of people in the world: those who understand binary and those who don't.",
        "Why do Java developers wear glasses? Because they can't C#!"
    ]
    return random.choice(jokes)

def ascii_art(text):
    return figlet_format(text)

def emojiify(text):
    emojis = {"happy": "😊", "sad": "😢", "code": "💻"}
    for word, emoji in emojis.items():
        text = text.replace(word, emoji)
    return text

def random_fact(topic):
    facts = {
        "python": "Python was created by Guido van Rossum in 1991.",
        "space": "The first human-made object in space was Sputnik, launched by the Soviet Union in 1957.",
        "coffee": "Coffee is the world's most popular beverage after water."
    }
    return facts.get(topic.lower(), "No fact available for this topic.")
