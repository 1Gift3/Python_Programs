# WHAT
# The script is designed to extract email addresses from lines in a text file and count how many such lines there are
# the code firstly as user for a file name
# open the file 
# creates an empty list to store email addresses
# looks for lines that start with From
# splits the lines into words
# gets the second word which is in the email
# stores it in the list
# and prints wach collected email addresss

# The reason we use "From" and not "From:" is that lines that start with "from " (note the space) contain sender info
# and lines that start with "From:" usually appear in headers and arent relevant for this task.

# HOW
# Can be usedfor email analysis:extracting and analysing senders from dataset
# Frequency analysis : who sent the most emails
# spam detection or filtering: looking at the sender domains or patters
# and data processing for machine learning tasks involving email datasets

# WHY
# for finding patterns or anomalies : security analyst or it admins, to look for supsicious senders in a server log
# easy to to handle Unix mbox files : mbox is still used in email backups especially research datasets,coorporate email archive tools and legacy systems
# its a great way to learn core python skills
# and its easy to customize from group senders by domain, building an address book, to clean up mailing lists.

# Expand
# we can include count for how many times each email appears
# can extract domains only
# save the emails to a new file

