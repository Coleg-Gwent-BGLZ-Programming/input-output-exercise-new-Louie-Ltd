
print("Welcome to the smoothie shop")
price = 3.50
reusable_cup = None
options =("yes", "no")
user_name = input(" please input your name ")
smoothie_amount = int(input("please input the amount of smoothies you wish to buy"))
while reusable_cup not in options:
  reusable_cup = input("would you like a reusable cup yes or no :")
if reusable_cup == "yes":
    total = smoothie_amount * price + 1
    print(f"thank you for your purchase {user_name} you were charged £{total}0 ")

else:
    total = smoothie_amount * price
    print(f"thank you for your purchase {user_name} you were charged £{total}0 ")

