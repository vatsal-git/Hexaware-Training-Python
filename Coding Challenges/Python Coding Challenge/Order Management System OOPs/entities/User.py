class User:
    def __init__(self, username, password, role):
        # self.__user_id = userId  #  Made ID auto-increment
        self.__username = username
        self.__password = password
        self.__role = role

    #  Made ID auto-increment
    # @property
    # def user_id(self):
    #     return self.__user_id
    #
    # @user_id.setter
    # def user_id(self, value):
    #     self.__user_id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value
