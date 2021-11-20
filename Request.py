from Time import *
class Request:
    def __init__(self, num_of_source, create_time, stat):
        self.__numOfSource = num_of_source
        self.__time = create_time
        self.stat = stat

    def get_time(self):
        return self.__time

    def get_priority(self):
        return self.__numOfSource

    def get_id(self):
        return str(self.__numOfSource) + ", " + '{:.3f}'.format(self.__time)

    def created(self):
        self.stat.created(self.__numOfSource)

    def leave_buffer(self):
        self.stat.add_wait_time(self.__numOfSource, Time.get_current_time() - self.__time)

    def in_worker(self, num, time):
        self.stat.add_work_time(self.__numOfSource, time - Time.get_current_time())

        self.stat.add_worker_time(num, Time.get_current_time())

    def leave_worker(self, num):
        self.stat.add_worker_time2(num, Time.get_current_time())

        self.stat.completed(self.__numOfSource)
        self.stat.add_all_time(self.__numOfSource, Time.get_current_time() - self.__time)

    def deny_buffer(self):
        self.stat.denied(self.__numOfSource)
        self.stat.add_wait_time(self.__numOfSource, Time.get_current_time() - self.__time)
