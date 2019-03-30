import random
user=input("Rock, Paper or Scissors")
user = user.capitalize()
comp=["Rock", "Paper", "Scissors"]
random.shuffle(comp)
if user == comp[0]:
    print("You chose " + user + " and tied")

if user == "Rock":
    if comp[0] == "Paper":
        print("You Lose! You chose " + user + ".")
    if comp[0] =="Scissors":
        print("You Win! You chose " + user + ".")

if user == "Paper":
    if comp[0] == "Rock":
        print("You Win! You chose " + user + ".")
    if comp[0] =="Scissors":
        print("You Lose! You chose " + user + ".")

if user == "Scissors":
    if comp[0] == "Rock":
        print("You Lose! You chose " + user + ".")
    if comp[0] == "Paper":
        print("You Win! You chose " + user + ".")