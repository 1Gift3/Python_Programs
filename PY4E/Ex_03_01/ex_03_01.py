hours = input("Enter hours:")
usr_rate = input("Enter rate:")

#print(hours, usr_rate)

ih = int(hours)
fr = float(usr_rate)

#print ("ih, fr")

if ih > 40 :
    #print("That's overtime")
    reg_pay = ih * fr
    otp = (ih - 40.0) * (fr * 0.5)
    #print(reg_pay, otp)
    Xy = reg_pay + otp
    print (Xy)    

else:
  #Print ("Reg_pay")
  Xy = ih * fr
  print(Xy)



