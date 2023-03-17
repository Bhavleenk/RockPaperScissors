import random

user_wins=0
computer_wins=0
options = ["rock","paper","scissors"]

while True:
  user_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
  if user_input == "q":
    break
    #quit()

  if user_input not in options:
    continue

  random_number = random.randint(0,2)
  #r:0, p:1, s:2
  computer_pick = optins[random_number]
  print("Computer picked", computer_pick, + ".")

  if user_input == 'rock' and computer_pick == ' scissor':
    print("You won!")

  print("Goodbye!")
  
    
  
