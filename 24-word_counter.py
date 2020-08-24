from collections import Counter
print ('Welcome the Frequancy Analysis App')

#list of elements to remove from all text
non_letters = ['1','2','3','4','4','5','6','7','8','9','0','.',',','?','!',';',':','(',')','@','$']

word = input('\nenter a word a phrase to count the occurrence of each letter: ').lower().strip()

for letter in non_letters :
    word = word.replace(letter, '')


total_occurrences = len(word)

#we will use the counter object so each letter will be a key to this dictinonary
#and the number of occurrences will be the value to this key 

#Creat a counter object to tally the number of each letter

letter_count = Counter(word)  #this will creat a dictionary of all letters and their occurance

for key, value in sorted(letter_count.items()):  #here we add sorted() to make it alphabetical order
    percentage = 100*value/total_occurrences
    percentage = round(percentage,2)
    print('\t','letter ' , key ,'is','\t' , str(value) ,'\t', str(percentage),'%')

#make a list of letters from highest occurance to lowest

ordered_letter_count = letter_count.most_common()
word_ordered_letters = []
for pair in ordered_letter_count:
    word_ordered_letters.append(pair[0])

print ('\nLetters ordered from haighst to lowest ')
for letter in word_ordered_letters :
    print(letter,end='')
    
