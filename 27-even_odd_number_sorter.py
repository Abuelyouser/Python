print('Welcome to the Even Odd Number Sorter App')

while True :
    numbers = input('Enter numbers separated by a comma(,) : ')

    #we have to remove the any white spaces by using replace()
    numbers = numbers.replace(' ','')

    #then we make numbers to be a list by using split()
    numbers_list = numbers.split(',')
    print('\t','-------summary-----')
    
    for i in numbers_list :
        i = int(i)
        if i % 2 == 0 :
            print('\t',i ,'is an even')
        else:
            print('\t', i , 'is an odd ')
  
    
