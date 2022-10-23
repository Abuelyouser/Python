#Dictionaries Challenge 22 : Database Admin Program

print ('Welcome to the Database Admin Program')

#create a dictionary to hold all username : password key value paris
log_on_information = {

    'mooman74':'alskes145',
    'mohamed32':'new22',
    'salma20':'mody20',
    'admin00':'P@ssw0rd'


    }

#get user input
username = input('Enter your username ' )

if username in log_on_information.keys() :
    password = input('Enter your password: ' )
    if password == log_on_information[username]:
        print('\nHello' , username , '! You are logged in: ')
        if username == 'admin00' :
            print('\nHere is the current user database : ')
            #show the whole database to the admin account 
            for key, value in log_on_information.items():
                print("Username: " , key , "\t\tPassword : " , value) #the \t make a tabe(space)
        else:
            #change password for a standard user
            change_password = input('Would you like to change password (yes/no). ' ).lower().strip()
            if change_password == 'yes' :
                new_password = input('please enter the password ' ) 
            
                
        
