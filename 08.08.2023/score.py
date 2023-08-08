s = float (input ("Enter the score : "))
if not s < 1.0 and s > 0.0 :
    if s >= 0.9 :
        print("A")
    elif s >= 0.8 and s < 0.9 :
        print ("B")
    elif s >= 0.7 and s < 0.8 :
        print ("C")
    elif s >= 0.6 and s < 0.7 :
        print ("D")
    else :
        print ("F")
else :
    raise Exception("No value less than 0.0 and more than 1.0. ")

    
