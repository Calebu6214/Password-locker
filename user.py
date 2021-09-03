import pyperclip
class User:
    """
    class that generates new instances of contacts
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

    # @classmethod
    # def copy_cred(cls,password):
    #     user_found = User.find_by_password(password,userlogin_name)
    #     pyperclip.copy(user_found.copycred)