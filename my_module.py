num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    num = -num

count = 0

# Special case for 0
if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print("Length of the number is:", count)
