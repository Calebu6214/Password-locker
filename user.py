import pyperclip
class User:
    """
    class that generates new instances of users
    """
    user_list = [] # Empty user list
    # Init method up here
    def __init__(self,userlogin_name,password):

          # docstring removed for simplicity

            self.userlogin_name = userlogin_name
            self.password = password
            # self.copycred = copycred

    def save_user(self):

            '''
            save_user method saves user objects into user_list
            '''

            User.user_list.append(self)


    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: Phone password to search for
        Returns :
            Credentials of user that matches the password.
        '''

        for user in cls.user_list:
            if user.password == password:
                return user

    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a user exists from the credentials list.
        Args:
            password: Password to search if it exists
        Returns :
            Boolean: True or false depending if the usere exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False

    # @classmethod
    # def copy_cred(cls,password):
    #     user_found = User.find_by_password(password,userlogin_name)
    #     pyperclip.copy(user_found.copycred)