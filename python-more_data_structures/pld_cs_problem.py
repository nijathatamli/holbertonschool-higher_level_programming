sentence = input('Sentence: ')
list_of_letters = [i for i in sentence if i.isalpha()]
list_of_sentences = [c for c in sentence if c in ['.', '!', '?']]
words = len(sentence.split())
L = (len(list_of_letters) / words) * 100
S = (len(list_of_sentences) / words) * 100
print((0.0588 * L) - (0.296 * S) - 15.8)