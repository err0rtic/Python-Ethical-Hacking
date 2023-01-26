import random
import string
from itertools import product

arg_dict = {'B': string.ascii_uppercase, 'L': string.ascii_lowercase, 'S': string.punctuation, 'N': string.digits}


def gen_wordlist(len_word, arg):
    wordlist_symbol = ''
    for i in set(list(arg.upper())):
        if i in arg_dict:
            wordlist_symbol += arg_dict[i]
    print(f'\nNumber of combinations: {((len(wordlist_symbol))**len_word)}')
    res = [''.join(var) for var in product(wordlist_symbol, repeat=len_word)]
    random.shuffle(res)
    return res


def write_file(len_word, arg):
    with open('gen_dict.txt', 'w') as writer_pars:
        for item in gen_wordlist(len_word, arg):
            writer_pars.write(item + "\n")
    print('Writing to file was successful')


if __name__ == "__main__":
    print('Keyword generator\n\nB - capital letters\nL - small letters\nS - special characters\nN - numbers')
    try:
        arg = input('\nChoose Arguments: ')
        len_word = int(input('Number of characters in a word: '))
        write_file(len_word, arg)
    except ValueError:
        print("Error, you did not enter a number\n")
    else:
        if len_word < 1:
            print('Error! Please enter a number greater than 0')
