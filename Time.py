from math import inf


class Time:
    __time = 0
    __step = 0
    __next_time = 0

    @staticmethod
    def get_current_time():
        return Time.__time

    @staticmethod
    def get_current_step():
        return Time.__step

    @staticmethod
    def reset_time():
        Time.__time = 0
        Time.__step = 0

    @staticmethod
    def upd_time(time):
        if Time.__next_time == Time.__time:
            Time.__next_time = inf
        if Time.__next_time > time:
            Time.__next_time = time

    @staticmethod
    def step():
        Time.__time = Time.__next_time
        Time.__step += 1
