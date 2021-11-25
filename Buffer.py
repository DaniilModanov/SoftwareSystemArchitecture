import config
from Request import *
class Buffer:
    def __init__(self, buffer_length):
        self.__buffer_length = buffer_length
        self.__buffer = [None] * self.__buffer_length


    def add_request(self, request):
        added = False
        first_available = -1
        if None in self.__buffer:
            for i in range(self.__buffer_length):
                if self.__buffer[i] is None:
                    first_available = i
                    break
            if first_available != -1:
                self.__buffer[first_available] = request
                added = True

        if added is False:
            self.deny_request(request)

    def deny_request(self, request):
        request.deny_buffer()

    def is_full(self):
        if None in self.__buffer:
            return False
        else:
            return True

    def get_request(self):
        max_priority = config.num_of_sources + 1
        for i in range(self.__buffer_length):
            if self.__buffer[i] is not None and self.__buffer[i].get_priority() < max_priority:
                max_priority = self.__buffer[i].get_priority()

        time_of_newest = 0
        for i in range(self.__buffer_length):
            if self.__buffer[i] is not None and self.__buffer[i].get_priority() == max_priority:
                time_of_newest = self.__buffer[i].get_time()

        for i in range(self.__buffer_length):
            if self.__buffer[i] is not None and self.__buffer[i].get_priority() == max_priority and self.__buffer[i].get_time() >= time_of_newest:
                time_of_newest = self.__buffer[i].get_time()
                r = self.__buffer[i]
                self.__buffer[i] = None
                r.leave_buffer()
                return r
        return None
