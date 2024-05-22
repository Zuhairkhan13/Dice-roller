import random

again = True

while again:
    print(random.randint(1,6))
    Another = input("Do you want to roll the dice agin? (y/n): ")
    if Another.lower() == "y":
        continue
    else:
        break