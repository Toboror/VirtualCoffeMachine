from coffee_machine import CoffeMachine
import time


# I had philosophy for 2 years in high school.
def desCartes():
    print('Hi. I am Unita. I think.')


def whatToDo():
    print('What do you want me to do?'
          '\n1 - Make money'
          '\n2 - Exit')


# Will automatically make money for the user for about 5 rounds
def makeMoney(userInput):
    if userInput == '1':
        print('Making money!')
        running = True
        CoffeMachine.cups *= 5
        CoffeMachine.water *= 5
        CoffeMachine.coffeeBeans *= 5

        # TODO MAKE IT STOP LOOPING AFTER IT DOES NOT HAVE ENOUGH WATER TO CONTINUE!
        # TODO THERE IS ALSO A BUG WHERE IF YOU MAKE COFFEE YOURSELF AND THEN FROM UNITA THE MONEY AMOUNT IS WRONG
        while running:
            # The logic is backwards, but it works so do not question it.
            CoffeMachine.buyAutomatic()
            time.sleep(1)
            print('Money is now $' + str(CoffeMachine.money))
            time.sleep(1)
            # Check if there's enough water to make at least an espresso
            # Assuming espresso requires the least amount of water
            if CoffeMachine.water < CoffeMachine.espressoWaterCost:
                print('Sorry, not enough  water!')
                running = False

    elif userInput == '2':
        exit()
