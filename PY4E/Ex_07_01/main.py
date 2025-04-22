# WHAT 
# fh = open : opens a file name mbox for reading. fh stands for file handle
# for lx in fh : loops through the file by line each line is temporaril stored in the var lx
# ly = lx.rstrip() : removes any trailling whitespaces from the end of the line, avoiding double spacing when printing
# print(ly) : conveerts the entire line to uppercase and prints

fh = open ('mbox-short.txt')


for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
    

# HOW
# When normalizing text making it uppercase or lower for analysis
# processing data before searching comparing and storing
# formatting output for reports or logs
# and reading and analysing email logs system logs or any structured text file

# WHY
# Its a foundational technique in programming, espcially in data processing automation and text analysis


