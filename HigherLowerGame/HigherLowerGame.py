import random
from day14_data import data,vs,gamename
print(gamename)
score=0
first = 2#random.randint(0, len(data) - 1)
second = random.randint(0, len(data) - 1)

while True:
    if first!=second:
        print(f"Compare A: {data[first]["name"]},a {data[first]["career"]} from {data[first]["place"]}")
        print(vs)
        print(f"Against B: {data[second]["name"]},a {data[second]["career"]} from {data[second]["place"]}")
        user_option=input("Enter your option 'A' or 'B': ").lower()
        if user_option=='a':
            if data[first]["followers"]>data[second]["followers"]:
                print("You won,",end=" ")
                score+=1
            else:
                print("You Lost")
                break
        elif user_option == 'b':
            if data[first]["followers"]<data[second]["followers"]:
                print("You won,",end=" ")
                score+=1
                first=second

            else:
                print("You lost")
                break
        print(f"Your current score is {score}")
        second = random.randint(0, len(data) - 1)

print(f"Your total score is {score}")


