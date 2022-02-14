while True:
    numbers = input('enter numbers: ').replace(';', ' ').split()
    if numbers[0] == numbers[1] and numbers[2] == numbers[3]:
        print('yay')
    elif numbers[0] == numbers[2] and numbers[1] == numbers[3]:
        print('jippi')
    elif numbers[0] == numbers[3] or numbers[1] == numbers[2]:
        print('great')
    elif numbers[0] > numbers[1] and numbers[2] > numbers[3]:
        print('are you proud of yourself?')
    elif numbers[0] < numbers[2] and numbers[1] < numbbers[3]:
        print('wow, mommy would be so proud of you')
    elif numbers[0] == numbers[3] or numbers[1] >= numbers[2]:
        print('you really think you are someone do you')
    elif numbers[0] <= numbers[3] and numbers[1] == numbers[2]:
        print('you feel great do you?')
    else:
        print("you are a failure, why can't you be more like my other users")
    if 'exit' in numbers:
        break
