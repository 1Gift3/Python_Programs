# WHAT
# defines a function to analyse a file - creating a reusable function that i can call for any file to analyse the spam confidence values
# opens the file safely and if not found it catches the error and prints a friendly message
# looks for spam confidence lines and only processes lines that start with this specific text
# extracts the number and adds it up by pulling the number from the line and adding it to a running total, keeping track of how many values it found
# then prints the average for each file


import os

def analyze_file(file_name):
    try:
        with open(file_name) as fh:
            count = 0 
            total = 0
            for line in fh:
                if line.startswith("X-DSPAM-Confidence:"):
                    number = float(line[line.find("0"):])
                    total += number
                    count += 1
            if count:
                print(f"{file_name} -> Average spam Confidence: {total / count:.4f}")
            else:
                print(f"{file_name} -> No data found.")

    except FileNotFoundError:
        print(f"{file_name} -> File not found.") 


# Automating for a list of files
files = ["log-Apr-21.txt", "log-Apr-22.txt", "log-Apr-23.txt"]
for file in files:
    analyze_file(file)                       

