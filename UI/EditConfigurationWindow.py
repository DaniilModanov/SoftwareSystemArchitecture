import tkinter as tk
import config

class EditConfigurationWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.grab_set()
        self.window.title("Edit Config")
        self.__create_ui()

    def __save(self):
        config.buffer_length = int(self.__bl.get())
        config.num_of_sources = int(self.__ns.get())
        config.num_of_devices = int(self.__nw.get())

        config.beta = float(self.__sc_beta.get())
        config.alpha = float(self.__sc_alpha.get())

        config.lam = float(self.__wc.get())
        config.auto_mode_steps = int(self.__au.get())

    def __create_ui(self):
        self.__bl = tk.StringVar()
        self.__ns = tk.StringVar()
        self.__nw = tk.StringVar()
        self.__sc_beta = tk.StringVar()
        self.__sc_alpha = tk.StringVar()
        self.__wc = tk.StringVar()
        self.__au = tk.StringVar()

        tk.Label(self.window, text="Buffer length").grid(row=0, column=0)
        tk.Label(self.window, text="Sources").grid(row=1, column=0)
        tk.Label(self.window, text="Workers").grid(row=2, column=0)
        tk.Label(self.window, text="Sources coef alpha").grid(row=3, column=0)
        tk.Label(self.window, text="Sources coef beta").grid(row=4, column=0)
        tk.Label(self.window, text="Workers coef").grid(row=5, column=0)
        tk.Label(self.window, text="Steps in automode").grid(row=6, column=0)

        bl = tk.Entry(self.window, textvariable=self.__bl)
        bl.insert(0, config.buffer_length)
        bl.grid(row=0, column=1)

        ns = tk.Entry(self.window, textvariable=self.__ns)
        ns.insert(0, config.num_of_sources)
        ns.grid(row=1, column=1)

        nw = tk.Entry(self.window, textvariable=self.__nw)
        nw.insert(0, config.num_of_devices)
        nw.grid(row=2, column=1)

        sc_alpha = tk.Entry(self.window, textvariable=self.__sc_alpha)
        sc_alpha.insert(0, config.alpha)
        sc_alpha.grid(row=3, column=1)

        sc_beta = tk.Entry(self.window, textvariable=self.__sc_beta)
        sc_beta.insert(0, config.beta)
        sc_beta.grid(row=4, column=1)


        wc = tk.Entry(self.window, textvariable=self.__wc)
        wc.insert(0, config.lam)
        wc.grid(row=5, column=1)

        au = tk.Entry(self.window, textvariable=self.__au)
        au.insert(0, config.auto_mode_steps)
        au.grid(row=6, column=1)

        tk.Button(self.window, text="Save", command=self.__save).grid(row=7, column=0, padx=5, pady=5)