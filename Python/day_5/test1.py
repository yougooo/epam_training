import sys
import itertools

def main(n):
    n_max = n
    guess_list = []
    print("Enter your guess digits or type 'help' if you wanna stop guess")
    while 1:
        guess = input("Your guess: ").split()
        if ''.join(guess) == n:
            print('You win! I guessed {0}'.format(n))
            return n
        elif ''.join(guess) == 'help':
            guess_list = [int(i) for i in guess_list if i.isdigit()]
            common_digits = {i:len(list(g)) for i,g in itertools.groupby(sorted(guess_list))}
            print("most frequently numbers: ", common_digits)
            return common_digits
        elif n in guess:
            guess_list.extend(guess)
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":

    n = sys.argv[1]
    main(n)

