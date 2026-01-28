# Plagiarism Checker
def is_plagiarized(text1, text2):
    """
    Check if two texts are plagiarized based on a simple similarity metric.
    
    Args:
    text1 (str): The first text to compare.
    text2 (str): The second text to compare.
    
    Returns:
    bool: True if the texts are considered plagiarized, False otherwise.
    """
    # Normalize the texts by converting to lowercase and removing punctuation
    import string
    
    def normalize(text):
        return ''.join(char.lower() for char in text if char not in string.punctuation).split()
    
    words1 = normalize(text1)
    words2 = normalize(text2)
    
    # Calculate the number of common words
    common_words = set(words1) & set(words2)
    
    # Calculate similarity ratio
    similarity_ratio = len(common_words) / max(len(set(words1)), len(set(words2)))
    
    # Define a threshold for plagiarism (e.g., 0.5 or 50% similarity)
    threshold = 0.5
    
    return similarity_ratio >= threshold
# Example usage
text_a = "This is a sample text for plagiarism checking."
text_b = "This text is a sample for checking plagiarism."

if is_plagiarized(text_a, text_b):
    print("The texts are plagiarized.")
else:
    print("The texts are not plagiarized.")
text_c = "Completely different content that shares no similarity."
if is_plagiarized(text_a, text_c):
    print("The texts are plagiarized.")
    