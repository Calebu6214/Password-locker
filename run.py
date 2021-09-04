#!/usr/bin/env python3.8
import pyperclip
from user import User
from credentials import Cred

def create_user(userlogin_name,password):
    '''
    Function to create a new user
    '''
    new_user =User(userlogin_name,password)
    return new_user


def create_cred(credname,userlogin_name,password):
    '''
    Function to create a new cred
    '''
    new_cred =Cred(credname,userlogin_name,password)
    return new_cred

        # save User
def save_users(user):
    '''
    Function to user
    '''
    user.save_user()


        # save User
def save_creds(cred):
    '''
    Function to cred
    '''
    cred.save_cred()    

def check_existing_users(userlogin_name,password):
    '''
    Function that check if a User exists with that userlogin and password and return a Boolean
    '''
    return User.user_exist(userlogin_name,password)
        #finding user
def find_cred(credname):
    '''
    Function that finds a cred by credname and returns the credentials
    '''
    return Cred.find_by_credname(credname)
        #check if credential exist
def check_existing_creds(credname):
    '''
    Function that check if a Cred exists with that credname and return a Boolean
    '''
    return Cred.cred_exist(credname)

       #display all contacts
def display_creds():
    '''
    Function that returns all the saved creds
    '''
    return Cred.display_creds()
#for deleting credentials
def delete_cred(cred):
    '''
    Function to delete a credential
    '''
    return Cred.cred_list.remove(cred)    
#for copying credentials
def copy_cred(cred_found):
    return  pyperclip.copy(cred_found.credname)


def main():
        print("Hello Welcome to your user list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : ca - create a new account,lg - for login to your account,ex - to exit ")

                short_code = input().lower()

                if short_code == 'ca':
                        print("New User")
                        print("-"*10)

                        print ("Username ....")
                        userlogin_name = input()

                        print("Password ...")
                        password = input()

                        
                        save_users(create_user(userlogin_name,password)) # create and save new user.
                        print ('\n')
                        print(f"New User {userlogin_name} {password} created")
                        print('\n')
                        print("proceed to login")
                       
                
                elif  short_code=='lg':
                       print("Enter user name")
                       defaultuser_name=input()

                       print("Enter password")
                       defaultuser_password=input()
                       print('\n')
                       if check_existing_users(defaultuser_name,defaultuser_password):
                           print(f"welcome:{defaultuser_name} into your account")
             
                           while True:
                                print("use these short codes: cn-create new credentials,dc - display credentials, fc -find a credential, ex -logout, dl -delete the credentials,cc -copy credentials")
                                short_code = input().lower()


                                if short_code=='cn':
                                   print("Enter new app name")
                                   credname=input()
                                   print("Enter username")
                                   userlogin_name=input()
                                   print("Password")
                                   password=input()

                                   save_creds(create_cred(credname,userlogin_name,password)) # create and save new user in new app.
                                   print ('\n')
                                   print(f"New Cred {credname} {userlogin_name} {password} created")
                                   print('\n')
                              

                                elif short_code == 'fc':

                                        print("Enter the appname you want to search for")

                                        search_credname = input()
                                        if check_existing_creds(search_credname):
                                                search_cred = find_cred(search_credname)
                                                print(f"{search_cred.credname} {search_cred.userlogin_name} {search_cred.password}")
                                                print('-' * 20)

                                                print(f"Appname.......{search_cred.credname}")
                                                print(f"Password.....{search_cred.password}")
                                                print(f"Username.......{search_cred.userlogin_name}")
                                        else:
                                                print("That credential does not exist")
                                elif short_code=='dc':
                                    if display_creds():
                                        print("Here is a list of all your credentials")
                                        print('\n')

                                        for cred in display_creds():
                                             print(f"{cred.credname} {cred.userlogin_name} .....{cred.password}")
                                        print('\n')

                                    else:
                                        print('\n')
                                        print("You dont seem to have any credentials saved yet")
                                        print('\n')
                                
                                elif short_code=='dl':
                                    print("Enter appname you want to delete its credentials")
                                
                                    search_credname=input()
                                    print('\n')
                                    if check_existing_creds(credname):
                                        search_cred=find_cred(search_credname)
                                        delete_cred(search_cred)
                                        print(f"This {search_cred.credname} app credentials has been deleted")
                                        print('\n')
                                    else:
                                        print("The credential doesn’t exist")

                                elif short_code=='cc':
                                    
                                    print("Enter the appname you want to copy its credentials")

                                    search_credname=input()
                                    print('\n')
                                    if check_existing_creds(search_credname):
                                        search_cred=find_cred(search_credname)
                                        copy_cred(search_cred)
                                        print("The credentials has been copied")
                                        print('\n')
                                    else:
                                        print("Credential doesn’t exist")

                                elif short_code =='ex':
                                       break
                                else:
                                    print("Enter valid code to continue")
                
                elif short_code=='ex':
                    break
                else:
                    print("Enter a valid code to continue")                    


if __name__ == '__main__':

    main() 

