print("Welcome to the Binary/Hexadecimal Converter App")
start = int(input('What decimal number would you like to start at :'))
end = int(input('What decimal number would you like to stop at: '))

decimal_values = []

for i in range(start,end+1):
    decimal_values.append(i)

print('\nDecimal values from',start , 'to',end)

for i in decimal_values:
    print('\t',i)

print('\nBinary values from',start , 'to',end )

for i in decimal_values:

    print('\t',bin(i).replace('0b',''))

    
print('\nHexadecimal values from',start , 'to',end )

for i in decimal_values:
    print('\t',hex(i).replace('0b',''))



    



