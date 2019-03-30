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
