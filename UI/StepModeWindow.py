from BusinessLogic.Time import Time
from BusinessLogic.Buffer import Buffer
from BusinessLogic.BufferManager import BufferManager
from BusinessLogic.DeviceManager import DeviceManager
from BusinessLogic.Device import Device
from BusinessLogic.Source import Source
from BusinessLogic.StatCollector import StatCollector
import config
import tkinter as tk


class StepModeWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.grab_set()
        self.window.title("Step mode")
        self.__init_system()
        self.__create_ui()

    def __init_system(self):
        Time.reset_time()
        self.stat = StatCollector()
        self.buffer = Buffer(config.buffer_length)
        self.sources = [Source(i, self.stat) for i in range(config.num_of_sources)]
        self.BufferManager = BufferManager(self.buffer, self.sources)
        self.workers = [Device(i) for i in range(config.num_of_devices)]
        self.DeviceManager = DeviceManager(self.buffer, self.workers)

    def __create_ui(self):
        tk.Label(self.window, text="Buffer").grid(row=0, column=0)

        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Имя')
        e0.grid(row=1, column=0)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Элемент')
        e0.grid(row=1, column=1)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')


        tk.Label(self.window, text=" " * 10).grid(row=0, column=4)
        tk.Label(self.window, text="Devices").grid(row=0, column=5)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Имя')
        e0.grid(row=1, column=5)
        v0 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=v0, state='readonly')
        v0.set('Элемент')
        e0.grid(row=1, column=6)

        self.lst_SV = []
        for i in range(config.buffer_length):
            self.lst_SV.append([tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()])
        lst_EN = []
        for i in range(config.buffer_length):
            lst = [tk.Entry(self.window, textvariable=self.lst_SV[i][0], state='readonly'),
                   tk.Entry(self.window, textvariable=self.lst_SV[i][1], state='readonly')]
            lst_EN.append(lst)
        for i in range(config.buffer_length):
            for j in range(2):
                lst_EN[i][j].grid(row=2 + i, column=j)
            self.lst_SV[i][0].set("Buffer " + str(i))
        self.__fill_buffer()

        self.lst_SV2 = []
        for i in range(config.num_of_devices):
            self.lst_SV2.append([tk.StringVar(), tk.StringVar()])
        lst_EN2 = []
        for i in range(config.num_of_devices):
            lst = [tk.Entry(self.window, textvariable=self.lst_SV2[i][0], state='readonly'),
                   tk.Entry(self.window, textvariable=self.lst_SV2[i][1], state='readonly'), ]
            lst_EN2.append(lst)
        for i in range(config.num_of_devices):
            lst_EN2[i][0].grid(row=2 + i, column=5)
            lst_EN2[i][1].grid(row=2 + i, column=6)
            self.lst_SV2[i][0].set("Device " + str(i))
        self.__fill_workers()

        down = max(config.buffer_length, config.num_of_devices) + 2

        tk.Button(self.window, text="Step", command=self.__one_step).grid(row=down, column=0, padx=5, pady=5)
        tk.Button(self.window, text="10 Steps", command=self.__ten_steps).grid(row=down, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Time:").grid(row=down, column=2)
        self.__time = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=self.__time, state='readonly')
        self.__time.set(0)
        e0.grid(row=down, column=3)

        tk.Label(self.window, text="Step:").grid(row=down, column=4)
        self.__step2 = tk.StringVar()
        e0 = tk.Entry(self.window, textvariable=self.__step2, state='readonly')
        self.__step2.set(0)
        e0.grid(row=down, column=5)

    def __fill_buffer(self):
        for i in range(config.buffer_length):
            v = self.buffer._Buffer__buffer[i]
            if v is None:
                self.lst_SV[i][1].set("None")
            else:
                self.lst_SV[i][1].set(v.get_id())


    def __fill_workers(self):
        for i in range(config.num_of_devices):
            v = self.workers[i]._Device__current_request
            if v is None:
                self.lst_SV2[i][1].set("None")
            else:
                self.lst_SV2[i][1].set(v.get_id())

    def __one_step(self):
        self.__step()
        self.__fill_buffer()
        self.__fill_workers()
        self.__time.set('{:.3f}'.format(Time.get_current_time()))
        self.__step2.set(Time.get_current_step())

    def __ten_steps(self):
        for i in range(10):
            self.__step()
        self.__fill_buffer()
        self.__fill_workers()
        self.__time.set('{:.3f}'.format(Time.get_current_time()))
        self.__step2.set(Time.get_current_step())

    def __step(self):
        self.BufferManager.work()
        self.DeviceManager.work()
        Time.step()
