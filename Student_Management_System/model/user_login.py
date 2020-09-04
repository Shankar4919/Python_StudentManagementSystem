
class login_detail:
    def __init__(self, username,password):
        self.__username=username
        self.__password=password

    def set_username(self, username):  # set username
        self.__username=username

    def get_username(self):  # get username
        return self.__username

    def set_password(self, password):  # set password
        self.__password=password

    def get_password(self):  # get password
        return self.__password

