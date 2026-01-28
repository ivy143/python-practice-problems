#word ladder problem
def word_ladder(begin_word, end_word, word_list):
    from collections import deque

    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    while queue:
        current_word, length = queue.popleft()
        if current_word == end_word:
            return length

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0
# Example usage
begin = "hit"
end = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

length = word_ladder(begin, end, word_list)
print("Length of shortest transformation sequence:", length)