a =int( input ("enter 1 for C to F : OR 2 for F to C  " ))
b = float(input ("enter the value of temperature "))
match a:
    case 1:
        res = (9/5) * b +32
        print(res)
    case 2: 
        res = (b-32)*(5/9)
        print(res)
    case _:
        print("kuch bhi ")
