height = int(input("MEntion your height: "))
age = int(input("Mention age: "))

if height > 120 and age > 18:
    print("Your ticket price is $12")

elif height > 120 and 12 <= age <= 18:
    print("Your ticket price is $7")

elif height > 120 and age < 12:
    print("Your ticket price is $5")

else:
    print("Cannot ride")
