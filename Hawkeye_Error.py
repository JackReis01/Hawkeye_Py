user = input("How is your day?")
if user == "":
    while user == "":
        user = input("Input an answer.")
print("Your day was " + user + ".")
print(user)

ladders=[9,4,8,2,6,1,7,3,19,2]
ladders[0]= 0
ladders.sort(reverse=True)
print(ladders[0])

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

mylist = []
n = int(input("Enter size of the list:\n"))

for i in range(0, n):
    temp = int(input("Enter number to append:\n"))
    mylist.append(temp)

print(mylist)
