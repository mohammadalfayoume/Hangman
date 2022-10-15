import time
import os

class Hangman:
    def __init__(self):
        self.guessing_word=None
        self.counter=5
        self.hints= None
        self.difficulty= None
        self.riddle = None
        self.words = []
        self.user_words = []
        self.is_finished = False
        # self.start()

    def welcome_message(self):
        time.sleep(1)
        os.system("clear")
        print('''
☆☆☆ Welcome to Hangman Game ☆☆☆
☆☆☆ Hangman is a game where you try to save someone from hanging ☆☆☆
☆☆☆ You will be asked to guess the correct word ☆☆☆
☆☆☆ Make sure you read the hints carefully, his life depends on it ☆☆☆
        \n\t''')
        input("Press any key to continue ...")
        
    def get_difficulty(self):
        time.sleep(1)
        userInput = input('Select Difficuilty  Easy:e   Hard:h  :  ')
        while True:
            
            if  self.input_validation(userInput):
                self.difficulty= userInput.lower()
                break
            else:
                time.sleep(1)
                userInput = input('Select Difficuilty  Easy:e   Hard:h  :  ')
    def input_validation(self,input):
        if input.lower() == 'e' or input.lower() == 'h':
            return True
        else:
            return False


    def select_hints(self,select):

        hint1 =["last hint: Please, save him, his soul is in your hands, the first part is 'water****' :)",
        "fourth hint: You can make a watery juice",
        "third hint:  It has a red pulp",
        "second hint: It has a smooth green skin",
        "first hint: The large fruit of a plant of the gourd family"]

        hint2 =["last hint: Please, save him, his soul is in your hands :(",
        "fourth hint: A person is tried for what he deserves if he is innocent",
        "third hint: Forgiving someone who has offended you",
        "second hint: something like forgivness",
        "first hint: the action of saving or being saved from sin"]
        if self.select_difficulty(select):
            self.riddle = 'This is the easy riddle, you have some hints and you have to guess the correct answer'
            self.hints = hint1
            self.words= ["watermelon"]
        else:
            self.riddle = 'This is the hard riddle, you have some hints and you have to guess the correct answer'
            self.hints = hint2
            self.words=["redemption","ransom","rescue","redeem"]
    def select_difficulty(self,difficulty):
        if difficulty== "e":
            return True
        else:
            return False
    def get_difficulty_data(self,difficulty):
        
        self.select_hints(difficulty)
        return [self.riddle,self.hints,self.words]


    def print_riddle(self):
        # get the riddle bassed on the difficulty
        # with first hint
        time.sleep(1)
        if self.counter==5:
            
            print(self.riddle)
        
        print(f"\nYou have {self.counter} guesses\n")
        time.sleep(1)
        print(self.hints[self.counter-1]+"\n")

    def get_input(self):
        # get input from user and check if valid
        # from pre selected words
        time.sleep(1)
        self.guessing_word=input("Enter the guessing word => ").lower()
        if self.guessing_word not in self.user_words:
            self.user_words.append(self.guessing_word)
            # print(self.user_words)
            
        else:
            while True:
                time.sleep(1)
                print(f"Sorry, this word is already guessed")
                time.sleep(1)
                self.guessing_word=input("Enter the guessing word => ").lower()
                if self.guessing_word not in self.user_words:
                    self.user_words.append(self.guessing_word)
                    break
                else:
                    continue
        
        return self.guessing_word
        
    def check_result(self,input):
        # check if game still running
        # check for result and print next hint if not correct
        if input == "quit" or input == "exit" or input == "q":
            self.is_finished = True
        else:
            
            if input in self.words:
                print(f"Congrats! your answer {input} is correct ^^")
                self.is_finished= True

            elif self.counter==5:
                time.sleep(1)
                print("   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n")
            
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
            
            if input not in self.words:
                if self.counter in range(2,6):
                    print(f"{input} is NOT correct, try again")
                elif self.counter==1:
                    print(f"{input} is NOT correct.\n\nGame over, the person is hanged :(")
    
    def start(self):
        self.welcome_message()
        self.get_difficulty()
        self.select_hints(self.difficulty)
        os.system("clear")
        while True:
            self.print_riddle()
            userInput = self.get_input()
            # print(userInput)
            # print(self.user_words)
            self.check_result(userInput)
            self.counter -=1
            if self.counter==0:
                self.is_finished=True
            if self.is_finished:
                break


hangman=Hangman()
hangman.start()

# print(hangman.get_difficulty_data("e")[2])
# print(x.user_words)
# x.welcome_message()
# x.get_difficulty()
# x.select_hints()
# x.print_riddle()
# x.get_input()
# print(x.user_words)