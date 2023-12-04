print("Thank you for choosing python pizza deliveries!")
size = input("size: S or M ")
add_pepperoni = input("pepperoni: S or M ")
extra_cheese = input("cheese: Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
