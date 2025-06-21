from random import choice

word_list = ["BANANA","LETTER","OASIS","JAVA","CITY","DRY","SMOG","CODE","COPE","ADAPT","GAME","COIN","DUTY","DIE","MOM","DADDY"]

chosen_word = choice(word_list)

print("A word is chosen, try to guess it based upon the rules given below: ")
print("\t1)You have six lives for guessing this word")
print("\t2)The number of Blanks indicates the number of letters the word consists of")
print("\t3)You need to enter a letter of the english alphabets,if the letter you have entered is not in the word that is selected by the computer,\n\t  you lose a life")
print("\t4)Try to guess the word before you run out of lives,if you manage to  guess the word before you run out of lives, then you win")
print("\tGood Luck!")

"""I know i can do like below but i thought it would be fun to do it that way
mystery_string = ("_ "* len(chosen_word)).rstrip()"""

def num_error():
    for n in range(1,10):
        if user_letter == str(n):
            print("Enter a letter,not a number")
            return True
    return False

mystery_string = "_"

count = len(chosen_word)
while count > 1:
    mystery_string += " _"
    count -= 1
    if count == 1:
        print(mystery_string)

mystery_string_2 = ""
for i in mystery_string:
    if i != " ":
        mystery_string_2 += i

mystery_list = list(mystery_string_2)

lives = 6
while lives > 0:
    user_letter  = input("Enter any letter here --> ")
    if len(user_letter) > 1:
        print("You are only allowed to enter one letter at a time")
        continue

    if num_error():
        continue

    for letter in chosen_word:
        if letter == user_letter.upper():
            mystery_list[chosen_word.index(letter)] = letter
            mystery_string = "".join(mystery_list)
            if chosen_word.count(letter) > 1:
                for n in range(1, len(chosen_word)):
                    if letter in chosen_word[n:]:
                        mystery_list[chosen_word.index(letter, n)] = letter
                        mystery_string = "".join(mystery_list)

    if user_letter.upper() not in chosen_word:
        lives -= 1

    print(mystery_string + "  " + f"lives left: {lives}")

    if mystery_string == chosen_word:
        print("congrats! You have won the game")
        break

if lives == 0:
    print(f"You lost!,The word was {chosen_word}" )











