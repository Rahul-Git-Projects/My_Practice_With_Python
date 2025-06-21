from random import choice

chosen_word = choice(["MOM"])
mystery_string = ("_ "* len(chosen_word)).rstrip()

print(mystery_string)


