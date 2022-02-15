from math import log

weekdays = ['monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday'
            'sunday']


a_frag = ['1','2','3']
b_frag = ['a','b','c']
c_frag = ['α','β','γ']

squared = []
loged = []
for i in a_frag:
    squared.append(int(i)*int(i))
    loged.append(log(int(i)))

print('i\t1\t2\t3')
print('i^2\t'+str(squared[0])+'\t'+str(squared[1])+'\t'+str(squared[2]))
print('log(i)\t'+str(loged[0])+'\t'+str(loged[1])+'\t'+str(loged[2]))

for a in a_frag:
    for b in b_frag:
        for c in c_frag:
            print(a+b+c)

masterlist = []
for i in squared:
    masterlist.append(i)
# another way of duing the same
# extend takes the content of a list and adds them as individual items to them
# other list
masterlist.extend(b_frag)
# this is functionally the same es masterlist = masterlist+b_frag

print("the master list is\n")
print(masterlist)

#deletion from list
lst = ['one','two','three']
print(lst)
try:
    lst.remove(input('remove which element?\n'))
except:
    print("removal failed")
else:
    pass
print(lst)

# insertion into list
print(lst)
print("now inserting 'foo' at position 1")
lst.insert(1, "foo")
print(lst)
