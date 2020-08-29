"""write a for loop that sums the values 1 through end, end is a variable
that we define for you so, for example if we define end to be 6 your code should
print out the result 21 which 1+2+3+4+5+6
"""
while True:
     end = int(input('enter the last number : '))
     total = 0

     for next in range(end+1):
          total += next
          print(total)
     
