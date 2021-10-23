import math

money_str = input("Enter the amount of money you have: P")
applePrice_str = input("What is the price of an apple? P")
money = float(money_str)
applePrice = float(applePrice_str)

numApple = money // applePrice
wNumApple = math.trunc(numApple)
change = money % applePrice

print(f"You can buy {wNumApple} apples and your change is {change:.2f} pesos.")