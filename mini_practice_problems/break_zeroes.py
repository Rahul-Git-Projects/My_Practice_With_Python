def break_zeroes(*args):
    for i,n in enumerate(args):
        if i < len(args) - 1:
            if args[i] == args[i + 1] and args[i] == 0:
                return True
    return False

print(break_zeroes(2,3,4,5,6,6,0,0,2,3,4) )





