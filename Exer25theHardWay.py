# Even more Practice

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted (words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# Run the program first to check if it's running without any errors
# then from the TERMINAL type python
# E:\GIT_DEV_python\python_train>python
# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import Exer25theHardWay
# >>> sentence = "All good things come to those who wait!"
# >>> words = Exer25theHardWay.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait!']
# >>> sorted_words = Exer25theHardWay.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait!', 'who']
# >>> Exer25theHardWay.print_first_word(words)
# All
# >>> Exer25theHardWay.print_last_word(words)
# wait!
# >>> wrods
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'wrods' is not defined
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> Exer25theHardWay.print_first_word(sorted_words)
# All
# >>> Exer25theHardWay.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait!']
# >>> sorted_words = Exer25theHardWay.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait!', 'who']
# >>> Exer25theHardWay.print_first_and_last(sentence)
# All
# wait!
# >>> Exer25theHardWay.print_first_and_last_sorted(sentence)
# All
# who
# >>>



