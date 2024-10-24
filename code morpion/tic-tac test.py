board = ["-","-", "-",
        "-","-", "-",
        "-","-", "-"]

curentplayer="X"
winner=None
gameRunning=True


# printing the game board
def printboard(board):
    print(board[0] + " | "+ board[1]+ " | " + board[2])
    print("__________")
    print(board[3] + " | "+ board[4]+ " | " + board[5])
    print("__________")
    print(board[6] + " | "+ board[7]+ " | " + board[8])


#take player input
def playerInput(board):
    inp=int(input("enter a number 1-9: "))
    if inp >=1 and inp <=9 and    board[inp-1]== "-":
        board[inp-1]= curentplayer
    else:
        print("oops player is already in that spot!")
# check for win or tie
def checkHorizontle(board):
   global winner 
   if board[0] == board[1] == board[2] and board[1]!= "-":
      winner= board[1]
      return True
   elif board[3] == board[4] == board[5] and board[3]!= "-":
      winner = board[3]
      return True
   elif board[6] == board[7] == board[8] and board[6]!= "-":
      winner=board[6]
      return True
   
def checkRow(board):
      global winner
      if board[0]==board[3]==board[6] and board[0]!= "-":
         winner=board[1]
         return True
      elif board[1]==board[4]==board[7] and board[1]!= "-":
         winner=board[1]
         return True
      elif board[2]==board[5]==board[8] and board[2]!= "-":
         winner=board[2]
         return True

def checkDiag(board):
        global winner
        if board[0]==board[4]==board[8] and board[0]!= "-":  
          winner=board[0]=curentplayer
          return True
        elif board[2]==board[4]==board[6] and board[2]!= "-":
           winner=board[2]=curentplayer
           return True
        
def checkTie(board):
      global gameRunning
      if "-" not in board:
           printboard(board)
           print("it is a tie!")
           gameRunning= False

def checkWine():
    global gameRunning
    if checkHorizontle(board) or checkDiag(board) or checkRow(board):
      print(f"the winner is {winner}")
      gameRunning= True
      

# switch the player
def switchPlayer():
   global curentplayer
   if curentplayer == "X":
      curentplayer = "O"
   else:
      curentplayer="X"

           
# check for win or tie again  
while gameRunning:
 printboard(board)
 playerInput(board)
 checkWine()
 checkTie(board)
 switchPlayer()