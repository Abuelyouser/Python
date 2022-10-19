"""
This is code snippets contains functions that i have made to deal with string manipulation espically in network automaiton and make life easier.
"""


"""
this method used to get the most frequent items.
"""
def most_frequent(alist):
    return max(set(alist), key=alist.count)


"""
This method used to return value(s) after the word mark and return an empty list if the mark word not found in text.
text >> we can pass this value from reader method
"""
def get_my_value(text, mark):
    text = text.split()
    values = []
    if text.count(mark) > 1:
        for i in range(text.count(mark)):
            values.insert(i,text[text.index(mark) + 1])
            text.remove(mark)
    elif text.count(mark) == 1:
        values.insert(0,text[text.index(mark) + 1])
    else:
        values = []
    return values
  
"""
this method works with get_my_value() method but it takes two marks. we use it to get the last service-port used in cabinet configuratin
and after knowing this service-port we add one to it and then we have a new service-port not repeated. 
"""
def get_my_value2(text,mark1,mark2):
    up = get_my_value(text,mark1)
    down = get_my_value(text,mark2)
    re = up + down
    return [int(s) for s in re if s.isdigit()]
  
"""
This is a simple method that change or replace the value of any string but return the string at the changed value only.
"""
def change_me(text,word,value):
    text = text.split()
    if type(word) is str:
        value = value.split()
        word = word.split()
    for i in range(len(word)):
        no = text.index(word[i]) + 1
        text.pop(no)
        text.insert(no,value[i])
    return " ".join(text)
