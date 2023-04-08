try :
    age = int(input("Enter your Age :  "))
    print(age )
    rate= 53
    est= rate/age
    print(est)

except ZeroDivisionError:
    print ("Age can not be Zeroo ")
except ValueError :
    print(" Invalid value ")


