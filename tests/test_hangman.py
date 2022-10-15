import pytest
from Hangman.hangman import hangman

def test_input_validation():
    assert hangman.input_validation("e")== True
    assert hangman.input_validation("h")== True
    assert hangman.input_validation("")== False


def test_select_easy_difficulty_data():
    assert hangman.get_difficulty_data("e")[0]=='This is the easy riddle, you have some hints and you have to guess the correct answer'
    assert hangman.get_difficulty_data("e")[1]==["last hint: Please, save him, his soul is in your hands, the first part is 'water****' :)",
        "fourth hint: You can make a watery juice",
        "third hint:  It has a red pulp",
        "second hint: It has a smooth green skin",
        "first hint: The large fruit of a plant of the gourd family"]
    assert hangman.get_difficulty_data("e")[2]==["watermelon"]


def test_select_hard_difficulty_data():
    assert hangman.get_difficulty_data("h")[0]=='This is the hard riddle, you have some hints and you have to guess the correct answer'
    assert hangman.get_difficulty_data("h")[1]==["last hint: Please, save him, his soul is in your hands :(",
        "fourth hint: A person is tried for what he deserves if he is innocent",
        "third hint: Forgiving someone who has offended you",
        "second hint: something like forgivness",
        "first hint: the action of saving or being saved from sin"]
    assert hangman.get_difficulty_data("h")[2]==["redemption","ransom","rescue","redeem"]
    