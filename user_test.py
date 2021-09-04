from credentials import Cred
import pyperclip
import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Caleb","12345") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.userlogin_name,"Caleb")
        self.assertEqual(self.new_user.password,"12345")
        # self.assertEqual(self.new_user.copycred,"copycred")

        #for saving new user

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    #for teardown
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

                 # test to find user
    def test_find_user_by_password(self):
        '''
        test to check if we can find a user by password and display information
        '''

        self.new_user.save_user()
        test_user = User("Caleb","12345") # new user
        test_user.save_user()

        found_user = User.find_by_password("12345")

        self.assertEqual(found_user.password,test_user.password)
        #checking if user exists
    def test_user_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Caleb","12345") # new user
        test_user.save_user()

        user_exists = User.user_exist("12345")

        self.assertTrue(user_exists)

     #for copying credentials
    # def test_copy_cred(self):
    #     '''
    #     Test to confirm that we are copying credentials from a found user
    #     '''

    #     self.new_user.save_user()
    #     User.copycred("12345")

    #     self.assertEqual(self.new_user.copycred,pyperclip.paste())

if __name__ == "__main__":
    unittest.main()