import random

TIMES_OF_GUESSING = 5

answer = random.randint(1, 100)
# print("Answer =", answer)

current_times_of_guessing = 0

while current_times_of_guessing < TIMES_OF_GUESSING:
    current_times_of_guessing += 1
    guessing_number = int(input(f"Guess ({current_times_of_guessing}):"))

    if guessing_number == answer:
        print(f"You Win Answer is {guessing_number}")
        break
    elif guessing_number >= answer:
        print("Too high")
    elif guessing_number <= answer:
        print("Too low")
else:
    print(f"You loss Answer is {answer}")
