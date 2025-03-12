#file =input("Enter file name:")
nfile =open("romeo.txt").read()
list_words = list() #empty list
afile= nfile.split()


for word in afile:
    if word not in list_words:
        list_words.append(word)
        list_words.sort()

print(list_words)        