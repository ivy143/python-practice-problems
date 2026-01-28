#import keyword module to check if a string is a valid keyword
import keyword

user_input = input("Enter a string to check if it's a valid keyword: ")
if keyword.iskeyword(user_input):
    print(f"'{user_input}' is a valid Python keyword.")
else:
    print(f"'{user_input}' is not a valid Python keyword.")
input("Press Enter to continue...")
#examples of keywords: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield