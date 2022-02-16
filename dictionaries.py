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
run = True  # just keep looping on ...
while run:  # and on until user exits out of the loop
    # ask user what he wants to do
    print("\nwhat do you want to do?\n"
          +"show phonebook (s)\n"
          +"add entry (a)\n"
          +"delete entry (d)\n"
          +"edit entry (e)\n"
          +"exit program (x)\n")
    inp = input() # save the answer into a variable inp
    if inp.lower() == 'x':  # check if the user wants to exit
        run = False         # don't continue the loop
    elif inp.lower() == 's':
        for e in phonebook: # for every key in the phonebook
            print(e)        # print it
            for i in phonebook[e]:  # and then loop over al entries in the subdict and print them
                print('\t', i, ':', phonebook[e][i].replace('\n','\n\t\t')) # this just formats the text for printing
    elif inp.lower() == 'a':
        new = input('enter name: ')
        phonebook[new] = {}             # add a new entry where key is the entered name
        for item in ['Address', 'Number', 'Birthdate', 'E-mail']:
            s = "enter "+item+': '  # ask for every field of the subdict what
            phonebook[new][item] = input(s) # for a value and add it to subdict
    elif inp.lower() == 'd':
        d = input('which entry to delete? ')
        try:        # try except else comes probably later
            del(phonebook[d])   # all you need to know is that here I
        except:                 # save the program if you enter an invalid key
            print('deletion failed please check spelling')
        else:
            pass
    elif inp.lower() == 'e':    # if user wants to edit
        e = input('which entry to edit? ')  # ask which entry
        e2 = input('change:')  # ask what user wants to change (e.g. address or email)
        for item in phonebook[e]: # check if the item entered is in the subdict
            changed = False     # remember if something changed
            if item == e2:
                phonebook[e][item] = input('new '+item+': ')
                changed = True  # if the key was in the subdict something has changed
            if changed == False:
                print('edit failed, please check spelling') # if the key was not in the subdict
                                        #we inform the user that nothing was changed

    elif inp.lower() == 'x':
        run = False
