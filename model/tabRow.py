class TabRow(object):
    def __init__(self):
        self.__teacher_name = None
        self.__time1 = None
        self.__time2 = None
        self.__time3 = None
        self.__time4 = None
        self.__time5 = None

    @property
    def teacher_name(self):
        return self.__teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name):
        self.__teacher_name = teacher_name

    @property
    def time1(self):
        return self.__time1

    @time1.setter
    def time1(self, time1):
        self.__time1 = time1

    @property
    def time2(self):
        return self.__time2

    @time2.setter
    def time2(self, time2):
        self.__time2 = time2

    @property
    def time3(self):
        return self.__time3

    @time3.setter
    def time3(self, time3):
        self.__time3 = time3

    @property
    def time4(self):
        return self.__time4

    @time4.setter
    def time4(self, time4):
        self.__time4 = time4

    @property
    def time5(self):
        return self.__time5

    @time5.setter
    def time5(self, time5):
        self.__time5 = time5
