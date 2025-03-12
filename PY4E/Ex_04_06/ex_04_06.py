def computepay(hours, rate):
    #print("In computepay", hours, rate)
    if hours > 40 :
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        #print(reg,otp)
        computepay = reg + otp
    else:
        computepay = hours * rate
    #print("Returning", pay)
    return computepay


fh = float(input ("Enter Hours:"))
fr = float(input("Enter Rate:"))

y = computepay(fh,fr)

#xp = computepay(fh,fr)

print ("Pay:", y)


 