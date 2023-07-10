# Using break
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

# Using pass
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        pass  # Placeholder, no action taken
    print(num)

# Using continue
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)

# Using for loop with else
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully.")

# Using while loop with else
num = 1

while num <= 5:
    print(num)
    num += 1
else:
    print("Loop completed successfully.")
