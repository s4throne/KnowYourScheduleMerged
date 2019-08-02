class Message(object):
    def __init__(self):
        self.__email = None
        self.__content = None
        self.__sender = None
        self.__created_at = None

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, full_name):
        self.__content = full_name

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, user_id):
        self._sender = user_id

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

