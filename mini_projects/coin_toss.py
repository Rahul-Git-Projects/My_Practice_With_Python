from random import choice

secret_codes = [1, 5, 3, 9, 2, 4]


def toss_coin():
    c_t = ["Heads", "Tails"]
    return choice(c_t)


def luck(string, secret):
    if string == "Tails":
        print("List will self-destruct")
        return []
    else:
        print("List was saved")
        return secret


print(luck(toss_coin, secret_codes))