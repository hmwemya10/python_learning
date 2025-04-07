# age = int(input('age :'))

# if age < 18 :
#     print('you are young')
# elif age > 18 and age < 30 :
#     print('you are normal age');
# else :
#     print('you are old');

    # print('hi'); 

# tired=input('are u tired? "y/n"') # y or n

# if tired == 'y' :
#     print('rest well');
# elif tired =='n' :
#     print('go back to work');
# else : 
#     print('pls enter y or n');

user_name = "hmmk";
password = "password12345";
enter_username = input("Please enter your username : ");
enter_password = input("Please enter your password :");

if (enter_username == user_name) and (enter_password == password) :
    print("You have logged in successfully!");
else: 
    print("Login Failed!");