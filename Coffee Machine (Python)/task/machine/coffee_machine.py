import time


class CoffeMachine:
    machineState = True

    enoughResources = 'I have enough resources, making you a coffee!'

    sorryNotEnough = 'Sorry, not enough '

    # Espresso stats
    espressoWaterCost = 250
    espressoCoffeeBeanCost = 16
    espressoPrice = 4

    # Latte stats
    latteWaterCost = 350
    latteMilkCost = 75
    latteCoffeeBeanCost = 20
    lattePrice = 7

    # Cappuccino stats
    cappuccinoWaterCost = 200
    cappuccinoMilkCost = 100
    cappuccinoCoffeBeanCost = 12
    cappuccinoPrice = 6

    # Cleaning need from 0 to 5
    machineCleaningNeed = 0

    def whatToDo(self):
        print('Write action (buy, maintenance, take, remaining, exit)')

    def __init__(self, name, water, coffeeBeans, milk, money, cups):
        self.name = 'The coffee machine'
        self.water = 400  # Ml
        self.coffeeBeans = 120  # Grams
        self.milk = 540  # Ml
        self.money = 550  # Dollar
        self.cups = 9  # Amount of disposable cups

    def userInput(self):
        _userInput = str(input())
        return _userInput

    def checkMissingIngredients(self):
        # Checks if enough water.
        if self.cappuccinoWaterCost > self.water or self.latteWaterCost > self.water \
                or self.espressoWaterCost > self.water:
            return ' water!'
        # Checks if enough coffe beans.
        elif self.cappuccinoCoffeBeanCost > self.coffeeBeans or \
                self.latteCoffeeBeanCost > self.coffeeBeans \
                or self.espressoCoffeeBeanCost > self.coffeeBeans:
            return ' coffe beans!'
        # Checks if enough milk.
        elif self.cappuccinoMilkCost > self.milk or self.latteMilkCost > self.milk:
            return ' milk!'
        # Checks if enough cups.
        if self.cups == 0:
            return 'Sorry, not enough cups!'

    def buy(self):
        print('What do you want to buy? '
              '| 1 - espresso - $' + str(self.espressoPrice),
              '| 2 - latte - $' + str(self.lattePrice),
              '| 3 - cappuccino - $' + str(self.cappuccinoPrice),
              '| back - to main menu:')
        _userInput = self.userInput()
        if _userInput == '1' or _userInput == '2' or _userInput == '3':
            self.cups -= 1
            # Espresso.
            if _userInput == '1':
                if self.water >= self.espressoWaterCost and \
                        self.coffeeBeans >= self.espressoCoffeeBeanCost and self.machineCleaningNeed < 5:
                    print(self.enoughResources)
                    self.makingCoffee()
                    self.coffeeBeans -= self.espressoCoffeeBeanCost
                    self.water -= self.espressoWaterCost
                    self.money += self.espressoPrice
                    self.machineCleaningNeed += 1
                elif self.machineCleaningNeed > 5:
                    print('Not able to make coffee. The machine needs cleaning.')
                else:
                    print(self.sorryNotEnough + str(self.checkMissingIngredients()))
            # Latte
            elif _userInput == '2':
                if self.water >= self.latteWaterCost and \
                        self.coffeeBeans >= self.latteCoffeeBeanCost \
                        and self.milk >= self.latteMilkCost and self.machineCleaningNeed < 5:
                    print(self.enoughResources)
                    self.makingCoffee()
                    self.coffeeBeans -= self.latteCoffeeBeanCost
                    self.water -= self.latteWaterCost
                    self.money += self.lattePrice
                    self.machineCleaningNeed += 1
                elif self.machineCleaningNeed > 5:
                    print('Not able to make coffee. The machine needs cleaning.')
                else:
                    print(self.sorryNotEnough + str(self.checkMissingIngredients()))
            # Cappuccino.
            elif _userInput == '3':
                if self.water >= self.cappuccinoWaterCost and \
                        self.coffeeBeans >= self.cappuccinoCoffeBeanCost \
                        and self.milk >= self.cappuccinoMilkCost and self.machineCleaningNeed < 5:
                    print(self.enoughResources)
                    self.makingCoffee()
                    self.coffeeBeans -= self.cappuccinoCoffeBeanCost
                    self.water -= self.cappuccinoWaterCost
                    self.money += self.cappuccinoPrice
                    self.machineCleaningNeed += 1
                elif self.machineCleaningNeed > 5:
                    print('Not able to make coffee. The machine needs cleaning.')
                else:
                    print(self.sorryNotEnough + str(self.checkMissingIngredients()))
            # Back to main menu.
            elif _userInput == 'back':
                self.whatToDo()

    def maintenance(self):
        print('What do you want to do? | 1 - fill | 2 - clean')
        _userInput = self.userInput()
        if _userInput == '1':
            self.fill()
        elif _userInput == '2':
            self.clean()

    def clean(self):
        print('Starting the cleaning process')
        str(time.sleep(1))
        print('[:----]')
        str(time.sleep(1))
        print('[::---]')
        str(time.sleep(1))
        print('[:::--]')
        str(time.sleep(1))
        print('[::::-]')
        str(time.sleep(1))
        print('[:::::]')
        str(time.sleep(1))
        print('Done!')
        str(time.sleep(1))

        self.machineCleaningNeed = 0

    def fill(self):
        print('Write how many ml of water you want to add:')
        _userInputWater = self.userInput()
        self.water += int(_userInputWater)
        print('Write how many ml of milk you want to add:')
        _userInputMilk = self.userInput()
        self.milk += int(_userInputMilk)
        print('Write how many grams of coffee beans you want to add:')
        _userInputCoffeeBeans = self.userInput()
        self.coffeeBeans += int(_userInputCoffeeBeans)
        print('Write how many disposable cups you want to add:')
        _userInputCups = self.userInput()
        self.cups += int(_userInputCups)

    # Takes out all the money in machine.
    def take(self):
        print('I gave you $' + str(self.money))
        self.money = 0

    # Displays remaining resources in the coffe machine.
    def resources(self):
        return ('{} has:'
                '\n{} ml of water'
                '\n{} ml of milk'
                '\n{} g of coffee beans'
                '\n{} disposable cups'
                '\n${} of money'.format(self.name, self.water, self.milk, self.coffeeBeans, self.cups, self.money))

    # Turns the machine 'off'
    def exit(self):
        self.machineState = False

    def makingCoffee(self):
        str(time.sleep(1))
        print('[:----]')
        str(time.sleep(1))
        print('[::---]')
        str(time.sleep(1))
        print('[:::--]')
        str(time.sleep(1))
        print('[::::-]')
        str(time.sleep(1))
        print('[:::::]')
        str(time.sleep(1))
        print('Done!')
        str(time.sleep(1))


CoffeMachine = CoffeMachine('The coffee machine', 400, 120, 540, 550, 9)

while CoffeMachine.machineState:

    CoffeMachine.whatToDo()

    userInput = CoffeMachine.userInput()

    if userInput == 'buy':
        CoffeMachine.buy()
    elif userInput == 'maintenance':
        CoffeMachine.maintenance()
    elif userInput == 'take':
        CoffeMachine.take()
    elif userInput == 'remaining':
        print(CoffeMachine.resources())
        print()
    elif userInput == 'exit':
        CoffeMachine.exit()
