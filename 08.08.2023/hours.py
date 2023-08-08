rate =(int) input("rate : ")
hours = (int) input("hours : ")
if hours <= 40:
    pay = hours * rate
elif hours > 40:
     pay = hours * rate + 10

else :  pay = hours
print (pay)
