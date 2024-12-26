from Resource import resources
from Resource import MENU
on = True
money = 0
while(on):
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water :{resources['water']}\nMilk:{resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money} ")
    elif choice == "espresso":
        print("enter your money:\n")
        quar = int(input(".25: "))
        dim = int(input(".10: "))
        nick = int(input(".05: "))
        pen = int(input(".01: "))
        total = quar * 0.25 + dim * 0.10 + nick * 0.05 + pen * 0.01
        returning = total - 1.5
        if returning < 0:
            print("Not enough money")
        else:
            print(f"returning {returning}")

