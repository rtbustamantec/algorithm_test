#!/usr/bin/python3

import re


def regex_letters(letters):
    letters = [re.escape(letter) for letter in letters]
    return '(?:{})'.format('|'.join(letters))


def check_word(word):
    regex_letter_g = regex_letters(['g', 'G'])
    regex_letter_o = regex_letters(['o', 'O', '0', '()', '[]', '<>'])
    regex_letter_l = regex_letters(['l', 'L', 'I'])
    regex_letter_e = regex_letters(['e', 'E', '3'])

    regex = '^{}$'.format(''.join((
        regex_letter_g,
        regex_letter_o,
        regex_letter_o,
        regex_letter_g,
        regex_letter_l,
        regex_letter_e
    )))

    return bool(re.match(regex, word))


if __name__ == '__main__':
    word = input("Enter a word: ")
    print(check_word(word))
