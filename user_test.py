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
        self.new_user = User("Caleb","12345","copycred") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.userlogin_name,"Caleb")
        self.assertEqual(self.new_user.password,"12345")
        self.assertEqual(self.new_user.copycred,"copycred")

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
    #for deleting user
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","12345") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

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