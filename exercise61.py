
mylist = [0,1,2,3,4,
          "zero", "one", "two", "three", "four"]

inp = input()
inp = inp.split()

for i in inp:
    if i in mylist:
        print("found", i)
    elif i in [str(item) for item in mylist]:
        print("there is", i, "but something is off")
    else:
        print(i, "not found")
