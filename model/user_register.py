class AddTeacher(object):
    def __init__(self):
        self.__fname = None
        self.__lname = None
        self.__email = None

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname = lname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
