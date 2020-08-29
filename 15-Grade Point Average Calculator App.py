print('Welcome to the Average Calculator App')

name = input('What is your name : ')
no_of_grades = int(input('\nHow many grades would you like to enter : '))

grades = []

grades_classes = ['first','second','third','fourth','fifth','sixth','seventh']

for i in range(no_of_grades):
    grades.append(int(input('enter your {} grade : '.format(grades_classes[i]))))
print(grades)

print('\nGrades Highest to lowest :')

grades.sort(reverse=True)
for grade in grades:
    print(grade)

print(name,"'Grade Summary :")
print('Total Number of Grades :',no_of_grades)
print('Highst Grade :', grades[0])
print('Lowest Grade : ',grades[-1])
average = sum(grades)/len(grades)
average = round(average, 2)
print(average)

desired_avg = float(input("\nWhat is your desired average: "))
