from math import exp
from random import random
import config
from BusinessLogic.Time import *

class Device:
    def __init__(self, num):
        self.__number = num
        self.__current_request = None
        self.__time_of_release = 0

    def is_available(self):
        return self.__current_request is None

    def add_request(self, request):
        self.__current_request = request
        self.__time_of_release = self.__calculate_work_time()
        self.__current_request.in_worker(self.__number, self.__time_of_release)
        Time.upd_time(self.__time_of_release)

    def __calculate_work_time(self):
        return Time.get_current_time() + config.lam * exp(int(random() * -config.lam))

    def try_to_release(self):
        if Time.get_current_time() >= self.__time_of_release and not self.is_available():
            self.__current_request.leave_worker(self.__number)
            self.__current_request = None
        elif not self.is_available():
            Time.upd_time(self.__time_of_release)
