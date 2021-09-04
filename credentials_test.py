import unittest # Importing the unittest module
from credentials import Cred # Importing the credentils class

class TestCred(unittest.TestCase):

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
        self.new_cred = Cred("FB","Caleb","12345") # create CREDENTIAL object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.credname,"FB")
        self.assertEqual(self.new_cred.userlogin_name,"Caleb")
        self.assertEqual(self.new_cred.password,"12345")
       

        #for saving new cred

    def test_save_cred(self):
        '''
        test_save_cred test case to test if the cred object is saved into
         the cred list
        '''
        self.new_cred.save_cred() # saving the new cred
        self.assertEqual(len(Cred.cred_list),1)
    #for teardown
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Cred.cred_list = []
        #for saving several credentials
    def test_save_multiple_cred(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our cred_list
            '''
            self.new_cred.save_cred()
            test_cred = Cred("FB","Caleb","12345") # new credential
            test_cred.save_cred()
            self.assertEqual(len(Cred.cred_list),2)
    #for deleting cred
    def test_delete_cred(self):
            '''
            test_delete_cred to test if we can remove a cred from our cred list
            '''
            self.new_cred.save_cred()
            test_cred = Cred("FB","Caleb","12345") # new cred
            test_cred.save_cred()

            self.new_cred.delete_cred()# Deleting a cred object
            self.assertEqual(len(Cred.cred_list),1)

                 #test to find cred
    def test_find_cred_by_credname(self):
        '''
        test to check if we can find a cred by credname and display information
        '''

        self.new_cred.save_cred()
        test_cred = Cred("FB","Caleb","12345") # new cred
        test_cred.save_cred()

        found_cred = Cred.find_by_credname("FB")

        self.assertEqual(found_cred.credname,test_cred.credname)
        #checking if cred exists
    def test_cred_exist(self):
        '''
        test to check if we can return a Boolean  if we cannot find the cred.
        '''

        self.new_cred.save_cred()
        test_cred = Cred("FB","Caleb","12345") # new CRED
        test_cred.save_cred()

        cred_exists = Cred.cred_exist("FB")

        self.assertTrue(cred_exists)


    def test_display_all_creds(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Cred.display_creds(),Cred.cred_list)

if __name__ == "__main__":
    unittest.main()