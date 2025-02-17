#_*_ coding: utf- 8 _*_


import random 
# make string input work with py 2 or 3

try: input = raw_input
except: pass
# a simple sample dict pick the right color
# keyword: [def1, def2, def3, correct_def_ix]
# could use model pickle to dump/load this dict

mydict = {
'sun': ['black', 'yellow', 'blue', 1],
'water': ['red', 'white', 'blue', 2],
'grass': ['white', 'green', 'orange', 1],
'coal': ['black', 'purple', 'red', 0]
}
keyword_list = list(mydict.keys())
# shuffle the keywords in place
random.shuffle(keyword_list)
print('Pick the right color for the folllowing:')
correct = 0 
wrong = 0
for keyword in keyword_list:
    sf = '''\
{}
A) {}
B) {}
C) {}
'''
    print(sf.format(keyword, mydict[keyword][0], mydict[keyword][1], mydict[keyword][2]))
    letter = input("Enter letter of your choice (A B C): ").upper()
    if letter == 'ABC'[mydict[keyword][3]]:
        print('correct')
        correct += 1

    else: 
        print('wrong')
        wrong += 1

 # final 
sf  = "Answers given --> {} correct and {} wrong"
print(sf.format(correct, wrong))           

# On thsi one i had not included parenthesis on line 33 which gave me wrong answer but i then fixed it.

