sentence = "  Python makes  coding easy  "

# Reverse the order of words
reversed_sentence = ' '.join(sentence.split()[::-1])

print(reversed_sentence)
# Output: easy coding makes Python


sentence = "Python makes coding easy"

# Reverse each word individually
reversed_each_word = ' '.join([word[::-1] for word in sentence.split()])

print(reversed_each_word)
# Output: nohtyP sekam gnidoc ysae
