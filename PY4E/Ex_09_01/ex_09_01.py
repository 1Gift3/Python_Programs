fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many = dict()

for line in fhand :
    line = line.rstrip()

    wds = line.split()

    for w in wds:
        #oldvalue = 0
        #if w in many : oldvalue = many[w]
        # we came up with a prettie r way of doing the same thing using get method
        many [w] = many.get(w,0) + 1 

print(many)        

#now we have to fine the word witht he largest count

largest = None
bigword = None
for cle, valeur in many.items() : 
    if largest is None or valeur > largest :
        largest = valeur 
        bigword = cle

print(bigword, largest)        