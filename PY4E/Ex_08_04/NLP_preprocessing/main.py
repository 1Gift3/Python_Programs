# WHAT
# Here we are preprocessing a text file for use in AI or NLP tasks by cleaning, tokenizing and duplicating the words
# The script loads the content of a .txt file, file_path is the path to the file and reads the file into a single string called text
# converts to lowercase making the entire text lowercase to standardize it
# removes punctuation string out punctuation like ! ? , . using string .punctuation list
# Tokenizing splitting into words, breaking the cleaned string into individual words tokens.
# it filters out common english words like the and is that dont add meaning in many NLP tasks
# stemms converting words to their base form running -> run
# duplicates and sorts by removing duplicates and sorting tokens alphabetically for easy viewing or indexing
# and returns the final list outputting a clean, unique, tokenized list of words - ready for analysis or machine learning input




import string 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStermmer

# making sure necessary Nltk packages are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(file_path, remove_stopwords=True, apply_stemming=False):
    # Step 1 : reading text file
    with open(file_path, 'r', encoding='utf-8' ) as file:
        text = file.read()

    # step 2 : lowercase
    text = text.lower()

    # removing punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # removing stopwords(optional) 
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [ word for word in tokens if word not in stop_words] 


    # stemming (optional)
    if apply_stemming:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(word) for word in tokens]

    # Deduplication
    unique_tokens = sorted(set(tokens))

    return unique_tokens

# example usage
if __name__ == "__main__":
    file_path = "romeo.txt" # replace it with my file path
    processed_tokens = preprocess_text(file_path)
    print(processed_tokens)

