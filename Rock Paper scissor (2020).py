def nameInput (): 
  global name
  name = "" #this line makes name variable
  nameCheck = "" #this line makes nameCheck variable
  while name == "" or len(name) > 25 or not name.isalpha() : 
    name = input("Enter your name: ").capitalize() #this line makes resriction for name
  while nameCheck == "" or len(name) > 25 or not name.isalpha() : 
    nameCheck = input("Enter your name again to vertify: ").capitalize() #this is checking name
  if nameCheck != name:
    nameInput() #If name and nameCheck doesn't matches, It goes back.
  else:
    roundsRequired() #If name and nameCheck matches, It goes to next part.
def roundsRequired():
  global rounds
  rounds = 0 #this line makes round variable
  roundsCheck = 0 #this line makes round variable
  while rounds < 1 or rounds > 7 or rounds %2 == 0:
    try:
      rounds = int(input("Enter number of rounds you wish play: ")) #this line will change user's input to integer
    except:
       pass
  while roundsCheck < 1 or roundsCheck > 7 or roundsCheck %2 == 0: #this makes the rounds number only odd.
    try:
      roundsCheck = int(input("Enter number of rounds you wish play: ")) #this line will get input from user to get round number again
    except:
       pass
  if roundsCheck != rounds:
    print("Round enter do not match. please enter again") #If rounds and roundsCheck doesn't matches, It goes back.
    roundsRequired()
  else:
    game() #If rounds and roundsCheck  matches, It goes to next part.
def game() :
  import random #This line will import a random value
  userScore = 0 #This line will set the variable "userScore"'s value 0.
  computerScore = 0 #This line will set the variable "computerScore"'s value 0.
  choices = ["Rock", "Paper", "Scissor"] #This line is a list of chocies that computer and user can make
  for gamesPlayed in range (rounds) :
    roundNumber = gamesPlayed + 1 #This line will increase the value of the "gamePlayed" when we play round
    userChoice = "" #This line will set the vaule of userChoice to 0
    while userChoice not in choices:
      userChoice = input("Round" + str(roundNumber) + "of" + str(rounds) + ". Enter your choice (Rock, Paper, Scissor) :").capitalize()#This line will ask to user to choose your choice.
    Computerchoise = random.randint(1,3) #This line will generate random number between 1 and 3
    if Computerchoise == 1: #if the random number is 1, it means rock
      Computerchoise = "Rock"
    elif Computerchoise == 2:  #if the random number is 2, it means rock
      Computerchoise = "Paper"
    else:
      Computerchoise = "Scissor" #if the random number is 3, it means sissor
    if userChoice == Computerchoise: #if the computer choise and user choise is same, print it is draw
      print("The result is draw, you both chose: ", Computerchoise)

    elif userChoice == "Rock" and Computerchoise == "Scissor":
      userScore = userScore + 1
      print(name, "won as Rock blunts sissors")#if the computer choise is sissor and user choise is rock, print user won

    elif userChoice == "Paper" and Computerchoise == "Rock":
      userScore = userScore + 1
      print(name, "won as Paper covers Rock")#if the user choise is paper and computer choise is rock, print user won

    elif userChoice == "Scissors" and Computerchoise == "Paper":
      userScore = userScore + 1
      print(name, "won as Sissors cut Paper")#if the user choise is sissor and computer choise is paper, print user won
    
    elif userChoice == "Rock" and Computerchoise == "Paper":
      print("Computer won as Paper covers Rock")
      computerScore = computerScore + 1 #if the user choise is rock and computer choise is paper, print computer won

    elif userChoice == "Paper" and Computerchoise == "Scissor":
      print("Computer won as Sissors cut paper")
      computerScore = computerScore + 1 #if the user choise is paper and computer choise is sissor, print computer won
    
    elif userChoice == "Scissor" and Computerchoise == "Rock":
      print("Computer won as Rock blunts sissors")
      computerScore = computerScore + 1 #if the user choise is sissor and computer choise is rock, print computer won

    else:
      computerScore = computerScore + 1
    print("You chose", userChoice, "and the toss resulted in", Computerchoise, "your score is", userScore, "and the computer score is", computerScore) #This line shows the overall score
  if computerScore > userScore:
    print("The computer won overall") #If computer's score is high print computer won
  elif computerScore < userScore:
    print(name, "won") #If user's score is high print user won
  else:
    print("the final result is a tie") #If computer's score and users' score is same print tie
  playAgain()

def playAgain():
  again = "" #this line makes again variable
  againCheck = "" #this line makes againcheck variable
  while again not in ["Y", "N"]:
    again = input("do you want to play again? Y or N").upper() #it will get input from user if you want to play agian
  while againCheck not in ["Y", "N"]:
    againCheck = input("do you want to play again? Y or N").upper() #it will get input from user if you want to play agian to check
  if againCheck != again:
    print("your answer doesn't match, do it again")
    playAgain() #if again and againCheck doesnt matches it repeats this part
  if again == "Y": #if again and againCheck matches it repeats whole process
    roundsRequired()
  else:
    print("goodbye!")
    quit() #it ends the code
nameInput()
