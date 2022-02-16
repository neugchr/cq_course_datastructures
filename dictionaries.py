from random import choice
from random import randint

######################
# This is just some code to fill the dictionary with random entries
# just ignore this and scroll down for the actually important code

firstname = ['Oma', 'Samuel', 'Nanny', 'Nobby', 'Feldwebel', 'Samuel', 'Lord']
lastname = ['Detritus', 'Weh', 'Wetterwachs', 'Ogg', 'Nobbs', 'Mumm', 'Käsedick', 'Vetinari']

emailpostfix = ['@unsichtbare.uni', '@nacht.wache', '@palast.info', '@magie.info']
numberprefix = '(0)171-'

city = ['Ankh-Morpork', 'Quirm', 'Pseudopolis',
        'Schmarm', 'Bes Pelargic', 'Krull']
street = ['Näherinnengasse', 'an der Nachtwachte',
          'bei den Gerbern', 'Vetinariplatz']

phonebook = {}

for entry in range(1,11):
    phonebook[choice(firstname)+' '+choice(lastname)] = {}

for k in phonebook:
    phonebook[k]['Address'] = (choice(city)+'\n'
                              +choice(street)+' '
                              +str(randint(1, 25)))
    phonebook[k]['Number'] = numberprefix + str(randint(3920000, 3920099))
    phonebook[k]['Birthdate'] = str(randint(1878, 1996))+'UC'

    if k == 'Lord Vetinari':
        phonebook[k]['E-mail'] = 'vetinari@lordschaft.ank'
        phonebook[k]['Address'] = 'Ankh-Morpork\nPalastplatz 1'
    elif k == 'Samuel Mumm':
        phonebook[k]['E-mail'] = 'hauptmann@nacht.wache'
        phonebook[k]['Address'] = 'Ankh-Morpork\nAnwesen Käsedick'
    elif k == 'Nobby Nobbs':
        phonebook[k]['E-mail'] = 'nobbi_nobbs@nacht.wache'
        phonebook[k]['Address'] = 'Ankh-Morpork\n'+choice(street)+str(randint(1,25))
    elif k == 'Oma Wetterwachs':
        phonebook[k]['E-mail'] = 'wetterwachs@he.xe'
    else:
        phonebook[k]['E-mail'] = (k.replace(' ', '_')+choice(emailpostfix)).lower()


######################
# ACTUAL CODE
######################
run = True
while run:
    print("\nwhat do you want to do?\n"
          +"show phonebook (s)\n"
          +"add entry (a)\n"
          +"delete entry (d)\n"
          +"edit entry (e)\n"
          +"exit program (x)\n")
    inp = input()
    if inp.lower() == 'x':
        run = False
    elif inp.lower() == 's':
        for e in phonebook:
            print(e)
            for i in phonebook[e]:
                print('\t', i, ':', phonebook[e][i].replace('\n','\n\t\t'))
    elif inp.lower() == 'a':
        new = input('enter name: ')
        phonebook[new] = {}
        for item in ['Address', 'Number', 'Birthdate', 'E-mail']:
            s = "enter "+item+': '
            phonebook[new][item] = input(s)
    elif inp.lower() == 'd':
        d = input('which entry to delete? ')
        try:
            del(phonebook[d])
        except:
            print('deletion failed please check spelling')
        else:
            pass
    elif inp.lower() == 'e':
        e = input('which entry to edit? ')
        try:
            e2 = input('change:')
            for item in phonebook[e]:
                if item == e2:
                    phonebook[e][item] = input('new '+item+': ')
        except:
            print('edit failed please check spelling')
        else:
            pass
    elif inp.lower() == 'x':
        run = False
