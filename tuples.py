tl = []

loop = 0
while loop <4:
    loop += 1
    tl.append(tuple(range(int(input('tuple of length: ')))))

for t in tl:
    print(t)
    print('which one do you like most?')
    i = int(input())
    if i < len(t):
        print(i, "is a nice number")
    else:
        print("this one isn't part off the tuple")

t = (1,1,True,False,None,'foo','bar','foo','bar')
print(t)

l = input('input some stuff').split()
t = tuple(l)
print(t)
