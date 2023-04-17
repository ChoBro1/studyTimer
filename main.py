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

    def _run_through_timer(self, fseconds, timer_id):
        while fseconds > 0 and not self.stopped:
            minutes = fseconds // 60
            seconds = fseconds % 60
            # Update Time Display
            if timer_id == 1:
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            elif timer_id == 2:
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            else:
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            fseconds -= 1

    # Have three different timers for each "session"
    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        # Start timer for pomodoro
        if timer_id == 1:
            # Time operates by seconds
            seconds = 60 * 25 #25 minutes
            self._run_through_timer(seconds, 1)
            # Go to next timer based off of self.count
            if not self.stopped or self.skipped:
                # Update Count Display
                self.count += 1
                self.pomodoro_counter_label.config(text=f"Count: {self.count}")
                if self.count % 4 == 0:
                    # Move to Long Break Timer
                    self.tabs.select(2)
                else:
                    # Move to Short Break Timer ( timer_id = 1 )
                    self.tabs.select(1)
                self.start_timer()
        elif timer_id == 2:
            seconds = 60 * 5  # 5 minutes
            self._run_through_timer(seconds, 2)
            if not self.stopped or self.skipped:
                # Return to Pomodoro Timer
                self.tabs.select(0)
                self.start_timer()
        else: # Long Break Timer
            seconds = 60 * 10  # 10 minutes
            self._run_through_timer(seconds, 3)
            if not self.stopped or self.skipped:
                # Return to Pomodoro Timer
                self.tabs.select(0)
                self.start_timer()

    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.count = 0
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="10:00")
        self.pomodoro_counter_label.config(text="Count: 0")
        self.running = False

    def skip_clock(self):
        # Reset the timers for each tab
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="10:00")

        self.stopped = True
        self.skipped = True

StudyTimer()


