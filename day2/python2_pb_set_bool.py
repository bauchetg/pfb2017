#!/usr/bin/python3                                                                                                                                                           

# test boolean values

#bool(0)
#test = bool('0')
#print(test)

#if  test == True:
#    print("True")
#else:
#    print("Not true")


# test boolean values using 
#my_list = [0, 0.0, FALSE, false, True, true, 'True', 'False']
test = 60 

if test > 0:
    message = "is positive"
    print (test, message)
    if test < 50:
        if test % 2 == 0:
             message = "is positive, smaller than 50 and is an even number"  
             print(test, message)
        else:
             message  = "is positve and smaller than 50 and an odd number"
             print(test, message)
    elif test == 50:
        if test % 2 == 0:
             message = "is positive, equal to 50 and is an odd number"
             print(test, message)
    else:
        if test % 3 == 0:      
             message = "is positive, greater than 50 and is divisible by three"
             print(test, message)
        else:
            message = "is positive and above 50 and is non divisable by three" 
            print (test, message)
else:
    message = "is negative" 
    print(test, message)

