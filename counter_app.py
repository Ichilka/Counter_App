import tkinter as tk

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
root.geometry("200x200")

# Create a label to display the counter
label = tk.Label(root, text=str(count), font=("Helvetica", 24))
label.pack(pady=5)

# Create increment button
increment_button = tk.Button(root, text="Add +1", command=increment)
increment_button.pack(side="left", padx=5)

# Create decrement button
decrement_button = tk.Button(root, text="Remove -1", command=decrement)
decrement_button.pack(side="right", padx=5)

# Create reset button for counter
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side="bottom", pady=5)

# Create a label to display the timer
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
timer_label.pack(pady=5)

# Create start button for timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(side="left", padx=5)

# Create stop button for timer
stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
stop_button.pack(side="right", padx=5)

# Create reset button for timer
reset_timer_button = tk.Button(root, text="Reset Timer", command=reset_timer)
reset_timer_button.pack(side="bottom", pady=5)

# Run the application
root.mainloop()
