import pyperclip
class Cred:
       """
    class that generates new instances of credentials
    """
       cred_list = [] # Empty cred list
    # Init method up here
       def __init__(self,credname,userlogin_name,password):

          # docstring removed for simplicity
            self.credname = credname
            self.userlogin_name = userlogin_name
            self.password = password

       def save_cred(self):

            '''
            save_user method saves user objects into user_list
            '''

            Cred.cred_list.append(self)


       def delete_cred(self):

        '''
        delete_cred method deletes a saved cred from the cred_list
        '''

        Cred.cred_list.remove(self)

       @classmethod
       def find_by_credname(cls,credname):
        '''
        Method that takes in a credname and returns a user that matches that credname.

        Args:
            crednmae: credname to search for
        Returns :
            Credentials of user that matches the credname.
        '''

        for cred in cls.cred_list:
            if cred.credname == credname:
                return cred

       @classmethod
       def cred_exist(cls,credname):
        '''
        Method that checks if a cred exists from the cred list.
        Args:
            credname: credname to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for contact in cls.cred_list:
            if contact.credname == credname:
                    return True

        return False


       @classmethod
       def display_creds(cls):
        '''
        method that returns the credential list
        '''
        return cls.cred_list

       @classmethod
       def copy_cred(cls,credname):
        cred_found = Cred.find_by_credname(credname)
        pyperclip.copy(cred_found.credname)