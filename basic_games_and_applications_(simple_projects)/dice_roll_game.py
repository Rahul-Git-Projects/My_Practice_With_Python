from random import randint


def throw_dice():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    return (dice_1, dice_2)

def roll_result(d1, d2):
    sum_dice = d1 + d2
    if sum_dice <= 6:
        return (f"The sum of your dice is {sum_dice}. Unfortunate")
    elif (6 < sum_dice < 10):
        return (f"The sum of your dice is {sum_dice}. You have a good chance")
    elif sum_dice >= 10:
        return (f"The sum of your dice is {sum_dice}. It looks like a winning roll")


D1, D2 = throw_dice()
result = roll_result(D1, D2)
print(result)