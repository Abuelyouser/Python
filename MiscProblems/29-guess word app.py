import random
print('Welcome to the Guess My Word App')

game_dict ={
    "sports":['basketball','baseball','soccer','football','tennis','curling'],
    'colors':['orange','yellow','purple','aquamamrine','violet','gold'],
    'fruits':['apple','banana','watermelon','peach','mange','strawberry'],
    'classes':['english','history','science','mathemtics','art','health'],
    }

#create a list of keys
game_keys = []    #loop through the keys of our dict

for key in game_dict.keys():
    game_keys.append(key)

#the main game loop
playing = True
while playing:
    game_category = game_keys[random.randint(0,len(game_keys)-1)]

#دلوقتي عشان اقدر اوصل للمحتوى الى حوا كل قسم
    game_value = game_dict[game_category][random.randint(0,len(game_dict[game_category])-1)]
    

    blank_word = []
    for letter in game_value :
        blank_word.append('-')

    print('Guess a ' , str(len(game_value)) , 'letter word from the following category',game_category.title())

    guess = ''
    guess_count = 0

    while guess != game_value :
        # instead of printing the whole list we join it using join print(blank_word)
        print(''.join(blank_word))
        
        guess = input('\nEnter your guess : ').lower()
        guess_count += 1


        #Guess if correct , user won the game
        if guess == game_value:
            print('\nCorrect! you guessed the word in ' , str(guess_count) , 'guesses')
            break

        else:
            print('\nThat is not correct let us reveal a letter to help you')

            #loop to replace - in the blank word to reveal a letter
            swapping = True
            while swapping :
                letter_index = random.randint(0,len(game_value)-1)
                if blank_word[letter_index] =='-':
                    blank_word[letter_index] = game_value[letter_index]
                    swapping = False

    choice = input('\nWould you like to play again (y/n) ').lower()

    if choice != 'y':
        playing = False
        print('thank you for playing ')
    
















                    
            
