ipt = ''
while True:
    ipt = input("enter range (strt; stp; it):")
    if 'exit' in ipt:
        break
    ipt = ipt.replace(';' , ' ')
    while '  ' in ipt:
        ipt = ipt.replace('  ', ' ')
    ipt=ipt.split(' ')
    print(ipt)
    for i in range(0, len(ipt)):
        try:
            ipt[i] = int(ipt[i])
        except:
            pass
        else:
            pass
    print(ipt)
    if len(ipt)==1:
        lst = list(range(ipt[0]))
    elif len(ipt)==2:
        lst = list(range(ipt[0],ipt[1]))
    elif len(ipt)==3:
        lst = list(range(ipt[0],ipt[1],ipt[2]))
    else:
        print('input does not match range')
    print("length of list is: ", len(lst))
    print("contents are: ", lst)
