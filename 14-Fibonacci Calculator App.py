print("Welcome to the Fibonacci Calculator App")
num = int(input('How many digits of the Fibonacci Sequence would you like to compute: '))

fib = [1,1]

for i in range(num-2):
    fib.append(fib[i]+fib[i+1])

print('\nThe first ',num,'numbers of the Fibonnaci Sequence are : ')    

for i in fib :
    print('\t',i)

golden = []

for i in range(len(fib)-1):
    golden.append(fib[i+1]/fib[i])

print('\nThe Golden ratio of  ',num,'numbers of the Fibonnaci Sequence are : ')

for i in golden:
    print('\t',i)



#another solution
    nterms = int(input('enter a number '))
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

for i in range(nterms):
    print(recur_fibo(i))

#another awesome solution
a, b = 0,1
while b <10:
    print(b)
    a , b = b, a+b


