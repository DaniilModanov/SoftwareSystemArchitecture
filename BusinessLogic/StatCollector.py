from collections import defaultdict
import config


class StatCollector:
    def __init__(self):
        self.sources_created = [0] * config.num_of_sources
        self.sources_denied = [0] * config.num_of_sources
        self.sources_completed = [0] * config.num_of_sources
        self.workers_worked = [0] * config.num_of_devices
        self.sources_wait_time = [0] * config.num_of_sources
        self.sources_all_time = [0] * config.num_of_sources
        self.sources_work_time = [0] * config.num_of_sources
        self.workers_last_request_time = [0] * config.num_of_devices

        self.sources_work_time_each_request = defaultdict(list)

        self.sources_wait_time_each_request = defaultdict(list)


    def created(self, i):
        self.sources_created[i] += 1

    def denied(self, i):
        self.sources_denied[i] += 1

    def completed(self, i):
        self.sources_completed[i] += 1

    def add_worker_time(self, num, time):
        self.workers_last_request_time[num] = time

    def add_worker_time2(self, num, time):
        self.workers_worked[num] += time - self.workers_last_request_time[num]

    def add_wait_time(self, num, time):
        self.sources_wait_time[num] += time
        self.sources_wait_time_each_request[num].append(time)

    def add_all_time(self, num, time):
        self.sources_all_time[num] += time

    def add_work_time(self, num, time):
        self.sources_work_time[num] += time
        self.sources_work_time_each_request[num].append(time)
