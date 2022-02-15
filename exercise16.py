

# d = {'one': 1, 2: "this is the second entry", '3': 3}
#
# print(d)
# inp = input('we need more k: v\n')
# inp = inp.split(': ')
#
# d[inp[0]]=inp[1]
# print(d)
#
# inp = input('destroy!?\n')
#
# delkey = None
# for k in d:
#     if k == inp or d[k] == inp:
#         delkey = k
# if delkey:
#     del(d[delkey])
#
# print(d)
#
# d = {}
# for i in range(1,11):
#     d[str(i)] = "this is entry "+str(i)
#
# dori = d.copy()
#
# runs = 0
# run = True
# while run:
#     runs +=1
#     inp = input("looking for: ")
#
#     if inp in d:
#         print('found ', inp, ": ", d[inp])
#         if input('Do you want to update it? (y) ') == 'y':
#             d[inp] = input('enter new value: ')
#     else:
#         print(inp, 'not found')
#         if input('Do you want to create it? (y) ') == 'y':
#             d[inp] = input('enter new value: ')
#     if input('Continue lookup? (n)' )== 'n':
#         if runs <=2:
#             print('sucks to be you, this has to happen thrice')
#         else:
#             run = False
#
# print("\noriginal dictionary:")
# for k in dori:
#     print(k, dori[k])
# print("\nnew dictionary:")
# for k in d:
#     print(k, d[k])
