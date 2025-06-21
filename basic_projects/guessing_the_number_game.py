from random import randint

user_name = input("Hello! Want to  play a game?if yes,please enter your name here: ")
random_number = randint(0,100)
print(f"Great!,Now {user_name},I have randomly chosen a number between 0 to 100,try guessing it!"
      "Rules of the game are given below:"
      "\n\t1.The guessed number must be in between 0 and 100(0 and 100 inclusive)"
      "\n\t2.You have only 8 attempts in guessing the number failing to do so will result in a loss")

attempt_num = 1
while attempt_num <= 8:
      guess = int(input(f"attempt number:{attempt_num},Guess the number: "))
      if (guess < 0 or guess > 100):
            print("The number you have just guessed is out of bounds,Try again")
            continue
      elif (guess == random_number):
            print(f"Congrats!you have guessed the number in {attempt_num} attempts")
            break
      elif (guess < random_number):
            print("The number you have picked is less than the number i have picked,Try again")
            attempt_num += 1
      elif (guess > random_number):
            print("The number you have picked is greater than the number i have picked")
            attempt_num += 1

if (attempt_num > 8):
      print(f"You failed to guess the number the number was {random_number}")








