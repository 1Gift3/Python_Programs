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


