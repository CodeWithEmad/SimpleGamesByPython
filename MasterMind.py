import random


class MasterMind:

    def check(self, rand, guess):
        black_white = [0, 0]
        for i, c in enumerate(guess):
            if c in rand:
                if c == rand[i]:
                    black_white[1] += 1
                elif c != rand[i]:
                    black_white[0] += 1
        return black_white

    def start(self):
        rand = str(random.randint(1000, 10000))
        guess = input('Guess what? ')
        guessnum = 1

        print(f'{self.check(rand, guess)[1]} Whites, {self.check(rand, guess)[0]} Blacks')

        while self.check(rand, guess)[1] != len(rand):
            guess = list(input('Guess another?'))
            print(f'{self.check(rand, guess)[1]:} Whites, {self.check(rand, guess)[0]:} Blacks')
            guessnum += 1
        print(f'Congrats dude! The number is: {rand:} After {guessnum:} guesses')
