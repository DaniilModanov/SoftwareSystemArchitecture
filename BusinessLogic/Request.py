from BusinessLogic.Time import *
class Request:
    def __init__(self, num_of_source, create_time, stat):
        self.__num_of_source = num_of_source
        self.__time = create_time
        self.stat = stat
        self.stat.created(self.__num_of_source)

    def get_time(self):
        return self.__time

    def get_priority(self):
        return self.__num_of_source

    def get_id(self):
        return str(self.__num_of_source) + ", " + '{:.3f}'.format(self.__time)

    def leave_buffer(self):
        self.stat.add_wait_time(self.__num_of_source, Time.get_current_time() - self.__time)

    def in_worker(self, num, time):
        self.stat.add_work_time(self.__num_of_source, time - Time.get_current_time())

        self.stat.add_worker_time(num, Time.get_current_time())

    def leave_worker(self, num):
        self.stat.add_worker_time2(num, Time.get_current_time())

        self.stat.completed(self.__num_of_source)
        self.stat.add_all_time(self.__num_of_source, Time.get_current_time() - self.__time)

    def deny_buffer(self):
        self.stat.denied(self.__num_of_source)
        self.stat.add_wait_time(self.__num_of_source, Time.get_current_time() - self.__time)
