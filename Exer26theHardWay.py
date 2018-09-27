# Practice debugging code of other
import Exer25theHardWay

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # fixed : error
    """Prints the first word after popping it off."""
    word = words.pop(0)  # fixed by removing the extra o in poop
    print(word)  # fixed syntax ()

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # fixed missing parenthesis
    print(word)  # fixed ()

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


print("Let's practice everything.")                                                   # fixed by adding ()
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')  # fixed by adding ()

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print("--------------")  # fixed by adding ()
print(poem)              # fixed by adding ()
print("--------------")  # fixed by adding ()

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five) # fixed by adding ()

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000  # fixed division operator
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # fixed by changing the sequence


print("With a starting point of: %d" % start_point)  # fixed by ()
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)) # fixed by ()

start_point = start_point / 10

print("We can also do that this way:")  # fixed by ()
print("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)) # fixed spelling of start_pont and added parenthesis


sentence = "All god\tthings come to those who weight."

words = Exer25theHardWay.break_words(sentence)
sorted_words = Exer25theHardWay.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) # fixed by removing period
print_last_word(sorted_words)
sorted_words = Exer25theHardWay.sort_sentence(sentence)
print(sorted_words) # fixed by adding ()

print_first_and_last(sentence) # fixed by fixing typo

print_first_and_last_sorted(sentence) # fixed typo and indention
