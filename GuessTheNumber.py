import random


class GTN:

    def __init__(self):
        print('*Guess the Number*')

    def start(self):
        while True:
            end_number = int(input('whats the last number: '))
            n = int(input('how many guesses: '))
            rand = random.randint(1, end_number)
            guess = int(input('your guess: '))

            while guess != rand:
                n -= 1
                if guess < rand:
                    print('UP UP UP')
                else:
                    print('DOWN DOWN DOWN')
                if n == 0:
                    print('You Lose, OutOfChoices!')
                    return
                else:
                    guess = int(input('your guess: '))

            print('You Won!!')
            if input('Do you want to continue? Y/N ') == 'Y':
                continue
            else:
                break
