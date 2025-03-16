# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# for num in nums:
#     if num % 2 == 0:
#         print(num)



import random

comp_guess = random.randint(1, 100)

attemps = 5

while attemps > 0:
    attemps -= 1
    user_guess = int(input("Enter your guess: "))
    if user_guess > comp_guess:
        print("Your number is bigger")
    elif user_guess < comp_guess:
        print("Your number is lower")
    else:
        print("You won the game")
        break
else:
    print(f"You lose the game The number was {comp_guess}")