

name = input('\nHello , enter your name : ')
number = int(input('enter your working number ' ))


print ('\nthe multiplication table for ' , number )


for i in range(1,10) :
    print ( i , ' * ' , number , ' = ' ,i*number)
    

print ('\nExponent Table for ' , number )

for i in range(1,10):
    print ( i , ' * *' , number , ' = ' ,i**number) 


print ('\nyour number is ' ,number)
