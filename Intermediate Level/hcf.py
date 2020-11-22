'''
24.Find H.C.F. (Highest Common Factor)
'''
num1 = int(input('Enter the number1: '))
num2 = int(input('Enter the number2: '))
def gcd(number1,number2):
    list1 = []
    list2 = []
    print(f"The H.C.F. of {number1} and {number2} is: ",end = '')

    for i in range(1,number1+1):
        if number1%i ==0:
            list1.append(i)
    for i in range(1,number2+1):
        if number2%i ==0:
            list2.append(i)


    if len(list1) > len(list2):
        for i in list1:
            for j in list2:
                if i == j:
                    hcf = i
        print(hcf)

    elif len(list1) < len(list2):
        for i in list1:
            for j in list2:
                if i == j:
                    hcf = i
        print(hcf)

    elif len(list1) == len(list2):
        for i in list1:
            for j in list2:
                if i == j:
                    hcf = i
        print(hcf)
gcd(num1,num2)