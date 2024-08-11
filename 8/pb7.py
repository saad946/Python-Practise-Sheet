l = ['apple', 'banana', 'cherry']

def remove_word_from_list(l, word):
    while word in l:
        print(word)
        l.remove(word)
    return l

print(remove_word_from_list(l, 'cherry'))  # Output: ['apple', 'banana']


