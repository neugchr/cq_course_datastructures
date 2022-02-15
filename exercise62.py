animals = ["ant", "bear", "cat", "dog", "elephant"]
numbers = [0, 1, 2, 3, 4, 5, 6]
bools = [True, False]

for lst in [animals, numbers, bools]:
    print(lst)

ok = False
while not ok:
    inp = input("insert what where? (str; pos)")
    inp = inp.split('; ')
    try:
        inp[1] = int(inp[1])
    except:
        print("unable to parse position please enter a number")
    else:
        pass

#try to cast input as an integer if succeds fine
    tp = type('')
    if inp[0] == "True" or inp[0] == "true" or inp[0] == "False" or inp[0] == "false":
        tp = type(bool())
    else:
        try:
            inp[0] = int(inp[0])
        except:
            pass
        else:
            tp = type(int())

    if tp == type(''):
        if inp[1] > len(animals):
            print('could not insert at position', inp[1], "index out of bounds")
        else:
            animals.insert(inp[1], inp[0])
            ok = True
    elif tp == type(bool()):
        if inp[1] > len(bools):
            print('could not insert at position', inp[1], "index out of bounds")
        else:
            bools.insert(inp[1], inp[0])
            ok = True
    elif tp == type(int()):
        if inp[1] > len(numbers):
            print('could not insert at position', inp[1], "index out of bounds")
        else:
            numbers.insert(inp[1], inp[0])
            ok = True
    else:
        print("something went horrible wrong, this should never happen")

print("lists are now")
for lst in [animals, numbers, bools]:
    print(lst)
