'''
22.To convert decimal to binary, octal and Hexa-Decimal
'''
global decimal
decimal = int(input("Enter the Digit: "))
def decimal_binary(decimal):
    print('Decimal TO Binary: ',end = ' ')
    binary_list = [decimal%2]
    while  True:
        decimal = decimal//2
        binary = decimal%2
        if decimal > 0:
            binary_list.append(binary)
        elif decimal ==0:
            binary_list.reverse()
            for i in binary_list:
                print(i, end ='')
            print()
            break

decimal_binary(decimal)

def decimal_octal(decimal):
    print('Decimal TO Octal: ',end =' ')
    octal_list = [decimal%8]
    while True:
        decimal = decimal//8
        octal = decimal%8
        if decimal > 0:
            octal_list.append(octal)
        elif decimal ==0:
            octal_list.reverse()
            for i in octal_list:
                print(i, end ='')
            print()
            break

decimal_octal(decimal)

# def decimal_hexa_decimal(decimal):
#     hexa = hex(decimal)
#     hexa = hexa.upper()
#     print('Decimal TO Hexadecimal: ',hexa[2:] ,end =' ')
#     print()

# decimal_hexa_decimal(decimal)

def decimal_hexa_decimal(decimal):
    print('Decimal TO Hexadecimal: ',end =' ')
    hexa_list = [decimal%16]
    while True:
        decimal = decimal//16
        hexa = decimal%16
        if decimal > 0:
            hexa_list.append(hexa)
        elif decimal ==0:
            hexa_list.reverse()
            for i in hexa_list:
                if i == 10:
                    i = "A"
                    print(i, end ='')
                elif i == 11:
                    i = "B"
                    print(i, end ='')
                elif i == 12:
                    i = "C"
                    print(i, end ='')
                elif i == 13:
                    i = "D"
                    print(i, end ='')
                elif i == 14:
                    i = "E"
                    print(i, end ='')
                elif i == 15:
                    i = "F"
                    print(i, end ='')
                else:
                    print(i, end ='')
            print()
            break

decimal_hexa_decimal(decimal)
