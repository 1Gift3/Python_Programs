file = input("Enter file name: ")
if len(file) < 1:
    file = "mbox-short.txt"
    
fhandle = open(file)

count = dict ()

for line in fhandle: 
    if line.startswith ("From "):
        words =line.split()
        #print(words)
        time = words[5]  
        hour = time.split(':')
        hours = hour[0]
        count[hours] = count.get(hours, 0) + 1

for k,v in sorted(count.items()):
    print(k,v)        

# In my code when i put this on dr chuck it gives me error stating wrong sumthing     

# So upon review line 10 where line.startswith adding space on the ""
# is crucial because it ensures that only the correct lines are processed.