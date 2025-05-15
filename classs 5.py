# IF-ELSE statements - decision making 


# Write a program in Python to check whether a student is passed or failed in his exam. 
# Given - Passing marks - 38 out of 100

marks =  int(input("Enter marks"))
if(marks >= 38 and marks <= 100):
    print("Pass")
elif(marks > 100 or marks<0):
    print("Invalid Entry")
elif(marks<38 and marks>0):
    print("Fail")
else:
    print("Fail")






    
# Use case - like while logging in if we provide wrong email -we can't login 

# correct email- xyz@abc.com - desired email - if user provides this then he/she can login else not
# password - 1234

# Focus on indentation 
# print(input("Enter you email"))

email = input("Enter your email : ")
if '@' in email:    # if email conatins @
    password = input("Enter password")

    if email == "xyz@abc.com" and password == "1234":
        print("Welcome. Login creds are correct")
    elif email == "xyz@abc.com" and password != "1234":  # else if - if the amil is correct but password in wrong
        print("Password Incorrect")
        password = input("Enter password again")
        if password == "1234":
            print("Finally correct. You may login")
        else: # if user still enters incorrect password
            print("Still incorrect password")
    else:
        print("Incorrect credentials")
else: # if the email entered was incorrect - then ask for email again
    print("Please enter your email again")




# Assignment:



# Indentation : a very important concept in Python - for good readability and also to detect and understand the block of code.
# using wrong indentation - logic may fail


# C program logic is like - using {}
'''
if(name == "xyz")
{
something;
    something;
} # closing curly bracket tells the termination of the if statement
else
{
something else;
    something else;
} 
'''


# In Python
name="xyz"
if name == "xyz":  # outer if statement
    print('line 10 adam ---- python ') # indentation comes automatically when : is used or if missed u can use TAB from keypad
    print("line20 adam")
    if 5 == 5: # nested if statement - inner if
        print('line 5')
else:
    print('line3')
