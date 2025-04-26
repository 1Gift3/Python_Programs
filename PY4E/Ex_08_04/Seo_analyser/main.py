# WHAT
# Building an seo keyword frequency analyzer that normalizing words, removing stop words and counting word frequency
# Importing reuired lib
# - string : provides access to common string operations including punctuation char
# - counter : works on a collection from pythons collections module helping count the frequency of items
# - stopwords: provides us with a list of common words that are generally considered unnecessary for keywords analysis
# - and nltk : is a powerful lib for text processing and natural language processing
# 

import string
from collections import Counter 
from nltk.corpus import stopwords
import nltk

# Downloading stopwords the first time you run this
nltk.download('stopwords')

# opening and reading the file content
with open("romeo.txt", "r") as file:
    text = file.read().lower()

# splitting text into individual words
raw_words = text.split()    

# removing punctuation from each word
cleaned_words = [word.strip(string.punctuation) for word in raw_words]

# loading english stopwords(e.g "the", "and" etc)
stop_words = set(stopwords.words('english'))

# filtering out stopwords and empty strings
filtered_words = [word for word in cleaned_words if word and word not in stop_words]

# counting the frequency of each word
word_counts = Counter(filtered_words)

# Printing the top N most common words
print("Top keywords by frequency:\n")
for word, count in word_counts.most_common(20): # changing 20 to anu number you want
    print(f"{word}: {count}")


