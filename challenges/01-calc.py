# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    ques = input('What calculation would you like to do ?(add, sub, mult, div)')
    ques1 = int(input('what is num1 ?'))
    ques2 = int(input('what is num2 ?'))

    if ques == 'mult':
        print (ques1 * ques2)
    elif ques == 'add':
        print (ques1 + ques2)
    elif ques == 'sub':
        print (ques1 - ques2)
    elif ques == 'div':
        print (ques2 / ques1)
    else:
        print('not a calculation')
    

calc()
        
