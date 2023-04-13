import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class StudyTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Study Time!")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file = "Kirby.png"))

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        # Have Tabs for Each Timer!
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        # Tab1: Main Study Timer
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 48))
        self.pomodoro_timer_label.pack(pady=20)
        self.tabs.add(self.tab1, text="Study Time")

        # Tab2: Short Break
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu", 48))
        self.short_break_timer_label.pack(pady=20)
        self.tabs.add(self.tab2, text="Mini Break")

        # Tab3: Extended Break
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
        self.long_break_timer_label = ttk.Label(self.tab3, text="10:00", font=("Ubuntu", 48))
        self.long_break_timer_label.pack(pady=20)
        self.tabs.add(self.tab3, text="Long Break")

        # Have Buttons for Timers
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)

        # Need to count # of successful study sessions to proceed into long break
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Count: 0", font = ("Ubuntu", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        # Initial statuses
        self.count = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        self.root.mainloop()

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        pass

    def reset_clock(self):
        pass

    def skip_clock(self):
        pass

StudyTimer()


