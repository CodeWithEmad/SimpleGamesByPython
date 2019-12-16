class RPS:
    def __init__(self):
        print('*Rock Paper Scissors*')

    def start(self):
        my_list = ['rock', 'paper', 'scissors']
        while True:
            p1 = input('Player 1: ').lower()
            p2 = input('Player 2: ').lower()
            while p1 not in my_list:
                p1 = input('wrong input. Player 1: ').lower()
            while p1 not in my_list :
                p1 = input('wrong input. Player 1: ').lower()

            if p1 == 'rock':
                if p2 == 'rock':
                    print('DRAW')
                elif p2 == 'Scissors':
                    print('Player 1 Won')
                elif p2 == 'paper':
                    print('Player 2 Won')
            elif p1 == 'paper':
                if p2 == 'paper':
                    print('DRAW')
                elif p2 == 'rock':
                    print('Player 1 Won')
                elif p2 == 'scissors':
                    print('Player 2 Won')
            elif p1 == 'scissors':
                if p2 == 'scissors':
                    print('DRAW')
                elif p2 == 'paper':
                    print('Player 1 Won')
                elif p2 == 'rock':
                    print('Player 2 Won')
            if input('Do you want to continue? Y/N') == 'Y':
                continue
            else:
                break
