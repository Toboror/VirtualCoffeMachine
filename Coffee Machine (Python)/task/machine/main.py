import subprocess
from coffee_machine import CoffeMachine
import unitA

while True:
    # Prints the main page message.
    print('This is the main page for the machines!'
          '\nWhich machine do you want to go to?'
          '\n1 - Coffee Machine'
          '\n2 - Exit'
          '\n3 - Special')

    userInput = input()

    # If the user inputs one of the valid 'inputtables.'
    if userInput == '1':
        subprocess.run(["python", "coffee_machine.py"])
    elif userInput == '2':
        exit()
    elif userInput == '3':
        print('You have chosen the special option!')
        unitA.desCartes()
        running = True
        while running:
            unitA.whatToDo()
            userInput = input()
            unitA.makeMoney(userInput)
        exit()
