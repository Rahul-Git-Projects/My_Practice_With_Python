def word_analysis(word):
    word_s = set(word)
    word_l = list(word_s)
    word_l.sort()
    return word_l

print(word_analysis("Hello World"))