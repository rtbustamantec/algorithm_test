#!/usr/bin/python3

from algorithm import regex_letters, check_word


def test_regex_letters():
    assert regex_letters(['g', 'G']) == '(?:g|G)'
    assert regex_letters(['o', 'O', '0', '()', '[]', '<>']) == '(?:o|O|0|\\(\\)|\\[\\]|<>)'


def test_check_word_when_is_correct():
    assert check_word('g00gle')
    assert check_word('google')
    assert check_word('g()()GI3')


def test_check_word_when_is_wrong():
    assert not check_word('g00gle ')
    assert not check_word('g google')
    assert not check_word('GGOOGLE')
    assert not check_word('hey google')
