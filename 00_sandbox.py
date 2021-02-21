import random

for item in range(0, 20):
    number = random.randint(1, 100)
    print(number)

    if number <= 1 or number >= 5:
        print("unicorn")
