# WHAT
# str = 'X-DSPAM : A string defined that contains a label and a number, separated by a colon
# - But note it is not best to use str as a variable as it overwrites the builtin str type
# ipos = str. : Finds the position(index) of the colon in the string, in our case its on index 18
# piece = float(str) : takes the part of the string after the colon using slicing and converts it to a float
# And finally prints out float value

#print(piece+42.0) #it fails cause its a string with a floating point
#value = float(piece)
#print(value)
#print(value+42.0)

# Seems like position +1 is thee printed position

# HOW
# It comes in handy when parsing text data , like if im processing files (like logs,sensor readings or scraped web data)numbers are often mixed with labels or formatting - hence i need a way to pull the numba out
# Data cleaning in  python, when data is messy or not in a clean spreadsheet, i would often have to use techniques like this to extract numbers from string
# Web scraping or email parsing.

# WHY
# It automates repetitive tasks
# Saves time on data entry
# allows me to analyse unstructured data 
# and forms the basis for AI, ML and data science pipelines
