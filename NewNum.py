userInput = 0
while True:
  try:
     userInput = int(input("Enter something: "))
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break
userInput=str(userInput)
print("Your number is " + userInput + ".")