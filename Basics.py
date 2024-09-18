import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data if not already downloaded
nltk.download('punkt')

# Sample sentence
sentence = "This is a sample sentence for tokenization."

# Tokenize sentence into words
words = word_tokenize(sentence)
print("Words:", words)

# Tokenize sentence into sentences
sentences = sent_tokenize(sentence)
print("Sentences:", sentences)
