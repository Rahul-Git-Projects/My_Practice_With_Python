def first_non_rep_char(string):
    for letter in string:
        if string.count(letter) == 1:
            return letter
    return None

print(first_non_rep_char("123451432"))