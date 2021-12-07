import tkinter as tk
from UI.EditConfigurationWindow import EditConfigurationWindow
from UI.AutomaticModeWindow import AutomaticModeWindow
from UI.StepModeWindow import StepModeWindow


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Архитектура программных систем")
        self.root.geometry("200x100")
        self.root.resizable(0, 0)
        tk.Label(self.root, text=" " * 15).grid(row=0, column=0)
        tk.Button(self.root, text="Automatic mode", command=self.__create_auto_window).grid(row=0, column=1)
        tk.Button(self.root, text="Step mode", command=self.__create_step_window).grid(row=1, column=1)
        tk.Button(self.root, text="Edit configuration", command=self.__create_config_window).grid(row=2, column=1)

    def start_ui(self):
        self.root.mainloop()

    def __create_config_window(self):
        EditConfigurationWindow()

    def __create_auto_window(self):
        AutomaticModeWindow()

    def __create_step_window(self):
        StepModeWindow()
