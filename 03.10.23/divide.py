try :
    
    a = int(input("Enter the divisor : "))
    b = int(input ("Enter the dividend : "))
    c = b / a
    print(f"Result = {c}")
except ValueError :
    print("Enter Valid Statements. ")
except ZeroDivisionError  :
    print("Err.. Zero divion ") 
