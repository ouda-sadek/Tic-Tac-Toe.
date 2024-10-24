#introduction
def intro():
    print("hello! welcome to Tic-Tac-Toe game :) ")
    inp=input("do you have a partener?if your answer is No your gonna to play with IA (yes/no):  ")
    if inp == "yes":
        print("it's gonna to be a great party! happy for you")
    elif inp=="no":
        print("can you win our IA? let's try ")
    else:
        print("please inter the right answer")
    
intro()
    
def symb():
    symbol=input("player 1 please chose your symbol (X/O): ")
    if symbol in("X" , "O"):
        print(f"you chose {symbol}, excellent choice! GOOD LUCK <3 ")
       
    else:
        print("please chose the right symbol")
symb()
