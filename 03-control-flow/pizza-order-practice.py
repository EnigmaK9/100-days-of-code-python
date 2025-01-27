print("Thank you for choosing Python Pizza Deliveries!")
size = input("Size: S or M ")
add_pepperoni = input("Pepperoni: S or M ")
extra_cheese = input("Cheese: Y or N ")
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
