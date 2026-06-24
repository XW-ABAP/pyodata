# %%
import tkinter as tk
from tkinter import messagebox

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("番茄工作法")
        self.root.geometry("300x200")
        
        self.time_left = 25 * 60
        self.is_running = False
        
        self.label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="开始", command=self.start_timer)
        self.start_button.pack()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.is_running = False
            self.label.config(text="00:00")
            messagebox.showinfo("时间到", "专注时间结束，休息一下吧！")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()


