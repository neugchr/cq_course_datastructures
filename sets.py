
# remove duplicates from list by castint it to set and back
ls = ['apple', 'apple', 'berry', 'coconut']
print(ls)
st = set(ls)
print(st)
ls = list(st)
print(ls)


setlist = []

loop = 0
while loop <4:
    loop +=1
    l = input('input some stuff\n').split()
    setlist.append(set(l))

for st in setlist:
    print(st)

s = {'foo', 11, 12, 1,2,3}
print(s)
print("adding something")
s.add("something")
print(s)
print("adding already existing integer 2")
s.add(2)
print(s)
buff = (s.pop(), s.pop())
print(buff)
print(s)
print('adding again')
s.add(buff[0])
s.add(buff[1])
print(s)
