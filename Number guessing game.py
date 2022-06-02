from  random import randint
from art import logo
EASY_TURNS=10
HARD_TURNS=5

def checkans(inp,ans,c):
    if inp>ans:
        print("Too High")
        return c-1
    elif inp< ans:
        print("Too Low")
        return c-1
    else:
        print(f"CORRECT : {ans}")
        return c-1
def diffi():
    m = input("Set Difficulty EASY=easy or HARD =hard : ")
    if m=="easy":
        return EASY_TURNS
    elif m=="hard":
        return HARD_TURNS
    else:
        print("Wrong selection")

def play_game():
     print(logo)
     print("WELCOME TO NUMBER GUESSING GAME")
     print("I'M THINKING OF A NUMBER BETWEEN 1 AND 100")
     ans = randint(1, 100)
     print(f"Correct answer is : {ans}")
     num = 0
     c = diffi()
     while num != ans and c>0:
         n = int(input("Enter a number between 1 and 100 : "))
         c=checkans(n, ans,c)
         if(c and num!=ans):
             print("GUESS AGAIN")
         print(f"You have {c} turns left ! ")

play_game()