numApple_str = input("How many apples you want to buy? ")
numOrange_str = input("How many orange you want to buy? ")
numApple = int(numApple_str)
numOrange = int(numOrange_str)

priceApple = numApple * 20
priceOrange = numOrange * 25
total =  priceApple + priceOrange

print(f"The total amout is {total:.2f}.")