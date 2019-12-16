from GuessTheNumber import GTN
from MasterMind import MasterMind
from RockPaperScissors import RPS

command = ''
while command.lower() != 'quit':
    print('''Choose one of the games below:
    1. Master Mind
    2. Rock, Paper, Scissors
    3. Guess the number
    ''')
    command = input('> ')
    if command == '1':
        master = MasterMind()
        master.start()

    elif command == '2':
        rps = RPS()
        rps.start()

    elif command == '3':
        gtn = GTN()
        gtn.start()
    else:
        pass
