import pytest
from pyfunbox.core import joke, ascii_art, emojiify, random_fact

def test_joke():
    assert isinstance(joke(), str)
    assert joke().strip() != ""

def test_ascii_art():
    result = ascii_art("Hello")
    assert result.strip() != ""  
    assert result.count("\n") > 0  

def test_emojiify():
    assert emojiify("I am happy") == "I am 😊"
    assert emojiify("This is sad") == "This is 😢"
    assert emojiify("I love to code") == "I love to 💻"

def test_random_fact():
    assert random_fact("python") == "Python was created by Guido van Rossum in 1991."
    assert random_fact("space") == "The first human-made object in space was Sputnik, launched by the Soviet Union in 1957."
    assert random_fact("unknown") == "No fact available for this topic."
