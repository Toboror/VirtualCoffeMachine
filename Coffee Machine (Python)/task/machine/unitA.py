from coffee_machine import CoffeMachine
import time


def desCartes():
    print('Hi. I am Unita.')


def whatToDo():
    print('What do you want me to do?'
          '\n1 - Make money'
          '\n2 - Exit')


def makeMoney(userInput):
    if userInput == '1':
        print('Making money!')
        while True:
            CoffeMachine.checkMissingIngredients()
            CoffeMachine.buyAutomatic()
            str(time.sleep(1))
            print('Money is now $' + str(CoffeMachine.money))
            str(time.sleep(1))
    elif userInput == '2':
        exit()
