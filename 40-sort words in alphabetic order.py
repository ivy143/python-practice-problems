#sort words in alphabetic order using recursion
def sort_words(words):
    if len(words) <= 1:
        return words
    else:
        pivot = words[0]
        less = [word for word in words[1:] if word <= pivot]
        greater = [word for word in words[1:] if word > pivot]
        return sort_words(less) + [pivot] + sort_words(greater)

# Example usage
input_words = input("Enter words separated by spaces: ").split()
sorted_words = sort_words(input_words)
print("Sorted words:", sorted_words)