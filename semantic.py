# In this program, we are just playing around with spaCy to
# understand its workings.

# Import spaCy.
import spacy

# Specify the model to be used.
nlp = spacy.load('en_core_web_md')

# Code snippet 1 - Comparing words 1
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("Comparing words 1")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print()

# Whilst I'm not surprised to find there's little similarity between
# "banana" and "cat", I find it interesting that there's a higher
# similarity between "cat" and "monkey" than there is between
# "monkey" and "banana"!

# Code snippet 2 - Comparing words 2
tokens = nlp('cat apple monkey banana')

print("Comparing words 2")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()

# Code snippet 2 - Comparing words 3

print("Comparing words 3")

tokens = nlp('cat chat chatter shatter')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()

# Code snippet 3 - Comparing sentences
print("Comparing sentences")

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# spaCy appears to be computing the similarity between the sentences
# based on the individual words involved rather than the actual meaning
# of the sentences as a whole.

# Code snippet 4 - Comparing sentences (example file)
# When running the example file, the more advanced model "en_core_web_md" gives
# higher similarity ratings than the simpler model "en_core_web_sm" which has no
# word vectors loaded, so the result of the Doc.similarity method does not give
# as useful similarity judgements as the more advanced model.