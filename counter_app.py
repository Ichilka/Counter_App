import tkinter as tk
from tkinter import ttk

def increment():
    global count
    count += 1
    label.config(text=str(count))

def decrement():
    global count
    count -= 1
    label.config(text=str(count))

def reset():
    global count
    count = 0
    label.config(text=str(count))

def set_counter():
    entry = ttk.Entry(main_frame, font=("Helvetica", 18), justify="center")
    entry.insert(0, str(count))
    label.update_idletasks()  # Update label geometry info
    entry_width = 80  # Manually set the width of the entry
    entry_height = 25  # Manually set the height of the entry
    x_offset = (label.winfo_width() - entry_width) // 2
    y_offset = (label.winfo_height() - entry_height) // 2
    entry.place(x=label.winfo_x() + x_offset, y=label.winfo_y() + y_offset, width=entry_width, height=entry_height)
    entry.focus()
    entry.bind("<Return>", lambda e: save_counter(entry))

def save_counter(entry):
    global count
    try:
        count = int(entry.get())
        label.config(text=str(count))
    except ValueError:
        pass
    entry.destroy()

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    global running
    running = False

def reset_timer():
    global time_count
    time_count = 0
    timer_label.config(text="00:00")
    stop_timer()

def set_timer():
    entry = ttk.Entry(main_frame, font=("Helvetica", 18), justify="center")
    entry.insert(0, timer_label.cget("text"))
    timer_label.update_idletasks()  # Update timer_label geometry info
    entry_width = 80  # Manually set the width of the entry
    entry_height = 25  # Manually set the height of the entry
    x_offset = (timer_label.winfo_width() - entry_width) // 2
    y_offset = (timer_label.winfo_height() - entry_height) // 2
    entry.place(x=timer_label.winfo_x() + x_offset, y=timer_label.winfo_y() + y_offset, width=entry_width, height=entry_height)
    entry.focus()
    entry.bind("<Return>", lambda e: save_timer(entry))

def save_timer(entry):
    global time_count
    try:
        time = entry.get().split(":")
        minutes = int(time[0])
        seconds = int(time[1])
        time_count = minutes * 60 + seconds
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    except (ValueError, IndexError):
        pass
    entry.destroy()

def update_timer():
    global time_count
    if running:
        time_count += 1
        minutes = time_count // 60
        seconds = time_count % 60
        timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)

# Initialize the counters and timer
count = 0
time_count = 0
running = False

# Create the main window
root = tk.Tk()
root.title("Counter App")
root.geometry("305x180")
root.attributes('-topmost', True)

# Create a style for modern look
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TLabel", font=("Helvetica", 18))

# Create a frame to center align the buttons and counter
main_frame = ttk.Frame(root)
main_frame.pack(pady=10)

# Create a label to display the counter
label = ttk.Label(main_frame, text=str(count), style="TLabel")
label.grid(row=0, column=1, padx=5)
label.bind("<Button-1>", lambda e: set_counter())  # Bind left-click to set counter

# Create increment button
increment_button = ttk.Button(main_frame, text="Add +1", command=increment)
increment_button.grid(row=1, column=0, padx=5)

# Create decrement button
decrement_button = ttk.Button(main_frame, text="Remove -1", command=decrement)
decrement_button.grid(row=1, column=2, padx=5)

# Create reset button for counter
reset_button = ttk.Button(main_frame, text="Reset", command=reset)
reset_button.grid(row=1, column=1, pady=5)

# Create a label to display the timer
timer_label = ttk.Label(main_frame, text="00:00", style="TLabel")
timer_label.grid(row=2, column=1, padx=5)
timer_label.bind("<Button-1>", lambda e: set_timer())  # Bind left-click to set timer

# Create start button for timer
start_button = ttk.Button(main_frame, text="Start Timer", command=start_timer)
start_button.grid(row=3, column=0, padx=5)

# Create stop button for timer
stop_button = ttk.Button(main_frame, text="Stop Timer", command=stop_timer)
stop_button.grid(row=3, column=2, padx=5)

# Create reset button for timer
reset_timer_button = ttk.Button(main_frame, text="Reset Timer", command=reset_timer)
reset_timer_button.grid(row=3, column=1, pady=5)

# Run the application
root.mainloop()
