import tkinter as tk
import statistics as stat
from BusinessLogic import StatCollector
from BusinessLogic.Buffer import *
from BusinessLogic.BufferManager import *
from BusinessLogic.Source import *
from BusinessLogic.Device import *
from BusinessLogic.DeviceManager import *
from BusinessLogic.StatCollector import *
from BusinessLogic.Request import *
from BusinessLogic.Time import *
import config


class AutomaticModeWindow:
    def __init__(self):
        self.stat = StatCollector()
        self.__work_system()
        self.window = tk.Toplevel()
        self.window.grab_set()
        self.window.title("Automatic mode")
        self.__create_ui()

    def __work_system(self):
        Time.reset_time()
        buffer = Buffer(config.buffer_length)
        sources = [Source(i, self.stat) for i in range(config.num_of_sources)]
        manager1 = BufferManager(buffer, sources)
        workers = [Device(i) for i in range(config.num_of_devices)]
        manager2 = DeviceManager(buffer, workers)

        for i in range(config.auto_mode_steps):
            manager1.work()
            manager2.work()
            Time.step()

    def __create_ui(self):
        tk.Label(self.window, text="Sources").grid(row=0, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Имя')
        e0.grid(row=1, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Создано')
        e0.grid(row=1, column=1)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Выполнено')
        e0.grid(row=1, column=2)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Отклонено')
        e0.grid(row=1, column=3)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Ср. время в системе')
        e0.grid(row=1, column=4)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Ср. время ожидания ')
        e0.grid(row=1, column=5)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Ср. время обработки')
        e0.grid(row=1, column=6)

        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Дисперсия ожидания')
        e0.grid(row=1, column=7)

        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Дисперсия обработки')
        e0.grid(row=1, column=8)

        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Вероятность отказа')
        e0.grid(row=1, column=9)

        for i in range(2, 2+config.num_of_sources):
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set("Source " + str(i-2))
            e0.grid(row=i, column=0)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.sources_created[i-2])
            e0.grid(row=i, column=1)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.sources_completed[i-2])
            e0.grid(row=i, column=2)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(self.stat.sources_denied[i - 2])
            e0.grid(row=i, column=3)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.sources_all_time[i - 2]/self.stat.sources_completed[i-2])[0:4])
            e0.grid(row=i, column=4)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            avg_wait = self.stat.sources_wait_time[i-2]/(self.stat.sources_completed[i-2]+self.stat.sources_denied[i-2])
            v0.set(str(avg_wait)[0:4])
            e0.grid(row=i, column=5)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            avg_work = self.stat.sources_work_time[i-2]/self.stat.sources_completed[i-2]
            v0.set(str(avg_work)[0:4])
            e0.grid(row=i, column=6)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(stat.pvariance(self.stat.sources_wait_time_each_request[i-2], avg_wait))[0:4])
            e0.grid(row=i, column=7)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(stat.pvariance(self.stat.sources_work_time_each_request[i-2], avg_work))[0:4])
            e0.grid(row=i, column=8)

            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.sources_denied[i - 2] / self.stat.sources_created[i - 2] * 100)[0:4] + "%")
            e0.grid(row=i, column=9)

        tk.Label(self.window, text="Devices").grid(row=2+config.num_of_sources, column=0)

        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set("Имя")
        e0.grid(row=config.num_of_sources+3, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set("Коэф. использования")
        e0.grid(row=config.num_of_sources+3, column=1)
        for i in range(config.num_of_sources+4, config.num_of_sources+4+config.num_of_devices):
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set("Device "+str(i - config.num_of_sources - 4))
            e0.grid(row=i, column=0)
            v0 = tk.StringVar()
            e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
            v0.set(str(self.stat.workers_worked[i - config.num_of_sources - 4]/Time.get_current_time()*100)[0:5] + "%")
            e0.grid(row=i, column=1)
