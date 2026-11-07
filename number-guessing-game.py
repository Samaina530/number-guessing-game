import random

running=True
while running:
    guesses=0
    entry = input("Enter a number(the range is from 1 to your entered number): ")
    if entry.isalpha():
        print("-------Invalid! Enter a valid number-------")
        continue
    elif entry.isdigit():
        entry = int(entry)
        r=random.randint(1,entry)
        playing=True
        while playing:

          guess = int(input("Guess a number: "))

          if guess==r:
            print("Correct")
            running=False
            break
          elif guess < r:
              print("--------The number is too low--------")
              guesses += 1
              playing=True
          elif guess > r:
              print("---------The number is too high--------")
              guesses += 1
              playing = True
          else:
            print("Try again")
    else:
        print("-------Invalid! Enter a valid number-------")
        continue

    print(f'You have made {guesses} guesses')

input("Press Enter to close the game...")


