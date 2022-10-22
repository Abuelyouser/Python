
"""
there are 3 ways to remove items from a list
grades.remove(m)    m.. is the item i need to remove  
grades.pop(n)       n..is the index of the item needs to be removed
dell grades[i:j]    i:j  the range of the items not included j
"""
print("Welcome to the Grade Sorter App")

grade_classes =['first','second','third','fourth']

grades = []
for i in range(len(grade_classes)):
    x =int(input('enter your {} grade(0-100): '.format(grade_classes[i])))
    grades.append(x)
print('\nyour grades are ',grades)
grades.sort(reverse=True)
print('\nyour grades from highest to lowest are :',grades)
print('\nThe lowest two grades will now be dropped.')


print('Removed grade : ',grades.pop())
print('Removed grade : ',grades.pop())

print('your remaning grade are : ',grades[:])
print('Nice work ! Your highest grade is a ',max(grades))



