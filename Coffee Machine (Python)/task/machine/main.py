import subprocess

while True:
    print('This is the main page for the machines!'
          '\nWhich machine do you want to go to?')

    print('1 - Coffee Machine'
          '\n2 - Exit')

    userInput = input()

    if userInput == '1':
        subprocess.run(["python", "coffee_machine.py"])


