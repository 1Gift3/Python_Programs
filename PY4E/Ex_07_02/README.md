# WHAT
# the code reads a file and cal the average of the spam confidence values found in lines that start with "X-DSPAM"
# It prompts the user to type in the name of the file
# opens the file whose name the user just typed
# initializes counters for how many matching lines were found(count) and the running total of the number extracted(total)
# loopes though each line in the file
# skips any line that does not start with "X-SPAM", soonly matching lines re processed further
# finds the position of the first "0" in the line. this assumes the number always starts with 0
# Extracts the number from the line starting at position t and converts it to float
# Updats the count of mactheed lines and adds the extracted number to the total
# calculates the average spam value
# and prints out the result

# HOW
# its great to learn pythons string handling & file i/o
# can be used to process email logs, web server logs, sensor data files and error logs

# Expand
# it to handle bad input (file not existant)
# extract it to extract dff kinds of data 
# visualize the data
# write results to a new file

# WHY
# Real use for this is to extract right useful info from raw to text
# Now real world use would be data analysis
# Automating repetitive tasks
# Log file processing
# And serves as a foundation for big projects - spam filtersm email processing and dashboard analytics tools