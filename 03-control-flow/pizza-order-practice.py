print("Thank you for choosing python pizza deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
