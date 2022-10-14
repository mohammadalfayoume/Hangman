import time

class Hangman:
    def __init__(self):
        self.guissing_word=None
        self.counter=5
        self.hints=["last hint: please, save him, his soul is in your hands :(",
        "fourth hint: A person is tried for what he deserves if he is innocent",
        "third hint: Forgiving someone who has offended you",
        "second hint: something like forgivness",
        "first hint: the action of saving or being saved from sin"]
    def get_words(self):

        self.words=["redemption"]

        return self.words
    def welcome_msg(self):
        print('''
☆☆☆ Welcome to Hangman Game ☆☆☆
☆☆☆ Hangman is a game where you try to save someone from hanging ☆☆☆
☆☆☆ You will be asked to guess the correct word ☆☆☆
☆☆☆ Make sure you read the hints carefully, his life depends on it ☆☆☆
        \n\t''')
    def set_guessing_word(self,guissing_word):
        self.guissing_word=guissing_word
        return guissing_word

    def guess_word_logic(self):
        
        if self.counter==0:
            print("Sorry, the person is hanged :(")
        else: 
            print(f"You have {self.counter} guesses")
            if self.counter==5:
                self.welcome_msg()
                print(self.hints[self.counter-1])
            self.set_guessing_word(input())

        if self.guissing_word not in self.get_words():
            if self.counter==5:
                time.sleep(1)
                print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
                
                # print("first hint: the action of saving or being saved from sin")
                
                
            elif self.counter==4:
                time.sleep(1)
                print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
                # print("second hint: the action of saving or being saved from sin")

            elif self.counter==3:
                time.sleep(1)
                print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
                # print("thired hint: the action of saving or being saved from sin")
            
            elif self.counter==2:
                time.sleep(1)
                print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

                # print("fourth hint: the action of saving or being saved from sin")

            elif self.counter==1:
                time.sleep(1)
                print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")

                print("\n Sorry, the person is hanged :(")

        else:
            self.guissing_word in self.get_words()
            print(f"Congrats! yor answer {self.guissing_word} is correct ^^")
         
        if self.guissing_word not in self.get_words() and self.counter in range(2,6):

            print(f"{self.guissing_word} is NOT correct, try again\n{self.hints[self.counter-2]}")

            self.counter -=1
            self.guess_word_logic()
        

hangman=Hangman()
hangman.guess_word_logic()



# class Guiss(Hangman):
#     def __init__(self):
#         super().__init__()
#     def guess_word_logic(self):
#         counter=1
#         while counter <= 5:
#             if self.set_guessing_word() in self.get_words():
#                 return "you are right"
#             else: pass
                

