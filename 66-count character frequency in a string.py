#count character frequency in a string
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage
string = "hello world"
frequency = char_frequency(string)
print(frequency)