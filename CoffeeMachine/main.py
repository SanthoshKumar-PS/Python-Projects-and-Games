water=300 #ml
milk=200 #ml
coffee=100 #g
money=0 #$
def calculatemoney():
    print("Please insert coins")
    quarter = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total=(pennies*0.01)+(nickles*0.05)+(quarter*0.25)+(dimes*0.10)
    return total


while True:
    user_choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice=="off":
        break
    elif user_choice=="report":
        print("Coffee Machine Reports")
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif user_choice=="espresso":
        if coffee>=18 and water>=50:
            user_money=calculatemoney()
            if user_money>0.50:
                print("Here is your Espresso Coffee!!! Enjoy drinking")
                money+=0.50
                returnmoney=user_money-0.50
                print(f"Please collect your change {round(returnmoney,2)}$")
                water-=50
                coffee-=18
            else:
                print("One espresso costs 0.50$,please enter correct money")

        else:
            if coffee<18:
                print("Sorry there is no enough coffee powder")
            elif water<50:
                print("Sorry there is no enough water")

    elif user_choice=="latte":
        if coffee>=24 and water>=200 and milk>=150:
            user_money=calculatemoney()
            print(user_money)
            if user_money>2.50:
                print("Here is your Latte Coffee!!! Enjoy drinking")
                money+=2.50
                returnmoney=user_money-2.50
                print(f"Please collect your change {round(returnmoney,2)}$")
                water-=200
                coffee-=24
                milk-=150
            else:
                print("One latte costs 2.50$,please enter correct money")

        else:
            if coffee<24:
                print("Sorry there is no enough coffee powder")
            elif water<200:
                print("Sorry there is no enough water")
            elif milk < 150:
                print("Sorry there is no enough milk")

    elif user_choice=="cappuccino":
        if coffee>=24 and water>=250 and milk>=100:
            user_money=calculatemoney()
            print(user_money)
            if user_money>3.00:
                print("Here is your Cappuccino Coffee!!! Enjoy drinking")
                money+=3.00
                returnmoney=user_money-3.00
                print(f"Please collect your change {round(returnmoney,2)}$")
                water-=250
                coffee-=24
                milk-=100
            else:
                print("One Cappuccino costs 3.00$,please enter correct money")

        else:
            if coffee<24:
                print("Sorry there is no enough coffee powder")
            elif water<200:
                print("Sorry there is no enough water")
            elif milk < 150:
                print("Sorry there is no enough milk")



