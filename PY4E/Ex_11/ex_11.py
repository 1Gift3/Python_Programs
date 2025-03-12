import re 
handle = input("Enter file name:")
fhandle = open(handle)

lst = []
for num in fhandle:
    keep = re.findall('[0-9]+', num)
    for answer in keep:
        #answer = int(answer)
        lst.append(int(answer))
        new = sum(lst)
print(new)        