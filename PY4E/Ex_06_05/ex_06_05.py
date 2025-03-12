str = 'X-DSPAM-Confidence:      0.8475'
#print(str)

ipos = str.find(':')
# print(ipos)
piece = float(str[ipos+1:])
print(piece)

#print(piece+42.0) #it fails cause its a string with a floating point
#value = float(piece)
#print(value)
#print(value+42.0)

# Seems like position +1 is thee printed position