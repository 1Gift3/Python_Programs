# WHAT
# here i am filtering specidic data X-DSPAM-Confidence
# extracting values from each match 
# aggregating data
# and summarising results


fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError:
    print("File not found:", fname) 
    quit()

count = 0
total = 0

for line in fh:
    if not line.startswith("X-SPAM-Confindence:"):
        continue
    t = line.find("0")
    number = float(line[t:])
    count += 1
    total += number

if count > 0:
    average = total / count
    print("Avergae spam confidence:", average)

else:
    print("No spam confidence lines found.")    