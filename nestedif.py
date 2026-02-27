height = int(input("What is your height: "))
age = int(input("What is your age: "))
if height > 120:
    if age > 18:
        print("You ticket rpice is $12")
    else:
        print("Your ticket price is $7")
else:
    print("Cannot ride")
