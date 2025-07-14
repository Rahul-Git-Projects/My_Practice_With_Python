def return_distinct(num1, num2, num3):
    if sum([num1,num2,num3]) > 15:
        return max(num1,num2,num3)
    elif sum([num1,num2,num3]) < 10:
        return min(num1,num2,num3)
    elif 10 <= sum([num1,num2,num3]) <= 15:
        list_n = [num1,num2,num3]
        list_n.sort()
        return list_n[1]
    return "Easter egg"

print(return_distinct(11, 2, 3))
