from Buffer import *
from BufferManager import *
from Device import *
from DeviceManager import *
from Source import *
from StatCollector import *
from Time import *

if __name__ == '__main__':

    stat = StatCollector()
    Time.reset_time()
    buffer = Buffer(config.buffer_length)
    sources = [Source(i, stat) for i in range(config.num_of_sources)]
    buffer_manager = BufferManager(buffer, sources)
    devices = [Device(i) for i in range(config.num_of_devices)]
    device_manager = DeviceManager(buffer, devices)


    for i in range(config.auto_mode_steps):
        buffer_manager.work()
        device_manager.work()
        Time.step()
        print("Время, которое проработали девайсы" + str(stat.workers_worked))
    print("Количество созданных заявок: " + str(stat.sources_created))
    print("Количество отклонённых заявок: " + str(stat.sources_denied))
    print("Количество выполненных заявок: " + str(stat.sources_completed))
    print("Всё время работы источников" + str(stat.sources_work_time))
    print("Всё время ожидания источников" + str(stat.sources_wait_time))
