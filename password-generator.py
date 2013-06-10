import argparse
import random

# Dictionary that maps characters to their equivalent number
number_dictionary = {
    'a': 4,
    't': 7,
    's': 5,
    'e': 3,
    'i': 1,
    'b': 8,
    'o': 0
}


def main():
    # Add command-line arguments
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('-w', '--wordlist', default='wordlist.txt',
            help='the wordlist which will be used')
    parser.add_argument('-l', '--max_length', default=1000, 
            help='the max word length', type=int)

    parser.add_argument('word_count', type=int)
    args = parser.parse_args()

    # Open wordlist and generate a list of all the words
    f = open(args.wordlist, 'r')
    wordlist = f.readlines()
    words = []
    print(len(wordlist))

    for i in range(0, args.word_count):
        while True:
            word = wordlist[random.randrange(0, len(wordlist))].strip()
            if(len(word) <= args.max_length):
                words.append(word)
                break


    password = list(" ".join(words))

    for i in range(1, random.randrange(1, 5)):
        location = random.randrange(0, len(password))
        password[location] = password[location].upper()

    for i in range(0, len(password)):
        if password[i] in number_dictionary:
            if random.randrange(0,2) == 1:
                password[i] = str(number_dictionary[password[i]])

    print(''.join(password))
if __name__ == "__main__":
    main()
