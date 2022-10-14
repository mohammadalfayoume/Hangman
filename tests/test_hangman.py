import pytest
from Hangman.classes import hangman

def test_hints():
    assert hangman.hints==["last hint: please, save him, his soul is in your hands :(",
        "fourth hint: A person is tried for what he deserves if he is innocent",
        "third hint: Forgiving someone who has offended you",
        "second hint: something like forgivness",
        "first hint: the action of saving or being saved from sin"]

def test_words():
    assert hangman.get_words()==["redemption"]

def test_guessing_word():
    assert hangman.set_guessing_word("riddit")=="riddit"
    