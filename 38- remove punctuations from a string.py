#remove punctuations from a string using recursion
def remove_punctuations(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if len(s) == 0:
        return s
    else:
        first_char = s[0]
        if first_char in punctuations:
            return remove_punctuations(s[1:])
        else:
            return first_char + remove_punctuations(s[1:])
# Example usage
input_string = "Hello, World! This is a test-string."
print("Original string:", input_string)
print("String without punctuations:", remove_punctuations(input_string))