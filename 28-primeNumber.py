"""Prime number is a number that is greater than 1
    and has two factors 1 and itself
    ex 2,3,5,7,11,13,17,19 and so one."""

print('Welcome to the Prime Number APP')

while True:
    print('\nEnter 1 to determine a specific number is prime or not. ')
    print('Enter 2 to determine all prime Number within a set of range')
    option = input('Enter your choice 1 or 2 : ')

    if option == '1':
        number = int(input('\nEnter a number : '))

        prime_status = True
        for i in range(2,number):
            print(i)
            if number % i == 0:
                prime_status = False
                break

        
