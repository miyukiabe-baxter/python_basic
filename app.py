menu = ""
is_started = False

while True:
    menu = input("> ").lower()
    print('is car,,,,,', is_started)
    if menu == 'start':
        if is_started:
            print('Car is already started...')
        else:
            is_started = True
            print('Car started')
    elif menu == 'stop':
        if not is_started:
            print('Car has already stopped')
        else:
            is_started = False
            print('Car has stopped')
    elif menu == 'help':
        print("""
  start - to start the car
  stop - to stop the car
  quit - to exit""")
    elif menu == 'quit':
        break
    elif menu == "":
        print('You did not specify the menu')
    else:
        print('I do not understand that...')

print('Quiting')
