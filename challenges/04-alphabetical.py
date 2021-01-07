# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def sorting():
    string = input('enter a word and it will return in alphabetical order')
    print(string)
    new_string = ''.join(sorted(string))
    print(new_string)
sorting()