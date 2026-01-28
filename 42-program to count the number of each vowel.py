#program to count the number of each vowel in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = {vowel: 0 for vowel in vowels}
    for char in s:
        if char in vowels:
            count[char] += 1
    return count

# Example usage
input_string = input("Enter a string: ")
vowel_counts = count_vowels(input_string)
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")