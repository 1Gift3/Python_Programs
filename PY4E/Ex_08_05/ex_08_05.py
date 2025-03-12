fhandle = open ('mbox-short.txt')

email_lst = list()

for line in fhandle: 
    if line.startswith ("From"):
        whole_line = line.split()
        Newmail = whole_line[1]
        email_lst.append(Newmail)

for string in email_lst:
    print(string)

print("There were", len(email_lst), "lines in the file with From as the first word" )            