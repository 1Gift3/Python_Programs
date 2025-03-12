file = input('enter file:')

handle = open(file)

dict = {}

for word in handle:
    if not word.startswith ('From:'):
        continue
    words = word.split()
    mail = words[1]
    dict[mail] = dict.get(mail, 0) + 1

min = 0 
max = 0

for mail, count in dict.items():
    if count > min:
        min = count
        max = mail

print(max,min)        

