def multiply(num1,num2):
    str1 = str(num1)
    str2 = str(num2)

    if len(str1) == 1 or len(str2) == 1:
        return num1*num2
    
    l1 = int(len(str1)/2)
    l2 = int(len(str2)/2)
    # we divide each number into two parts
    # num1
    a = int(str1[:l1])
    b = int(str1[l1:])
    # num2
    c = int(str2[:l2])
    d = int(str2[l2:])

    ac = multiply(a,c)
    bd = multiply(b,d)
    if (len(str1) == len(str2) and len(str1) % 2 == 0):
        # here we will have one less recursive call
        product = (10**(l1 + l2)) * ac + (10**l1) * (multiply(a+b,c+d) - ac - bd) + bd
    else:
        product = (10**(l1 + l2))* ac + (10**l2) * multiply(b,c) + (10**l1)*multiply(a,d) + bd
        
    return product 
