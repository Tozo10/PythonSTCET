h = int (input ("Enter the hour : "))
r = int (input ("Enter the rate : "))

if h > 40 :
    pay = (1.5 * r)*(h-40) + (r * 40)
else :
    pay = r * h
print ("Payment Must Be : ",pay)
