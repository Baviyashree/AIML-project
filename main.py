import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from datetime import datetime

# Create a directory to store captured images
if not os.path.exists('captured_images'):
    os.makedirs('captured_images')


def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    image_filename = f'captured_images/attendance_{timestamp}.jpg'
    cv2.imwrite(image_filename, frame)
    cap.release()

    # Display the captured image on the GUI
    img = Image.open(image_filename)
    img = img.resize((300, 400))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img


def mark_attendance():
    # Get name and register number from input fields
    name = name_entry.get()
    reg_number = reg_entry.get()

    # printing a message with name and register number
    print(f"Attendance Marked for {name} with Register Number {reg_number} on {datetime.now()}")


# main Tkinter window
root = tk.Tk()
root.title("Attendance Register")

# tkinter label for name
name_label = Label(root, text="NAME:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

# tkinter label for register number
reg_label = Label(root, text="REGISTER NUMBER:")
reg_label.grid(row=1, column=0)
reg_entry = Entry(root)
reg_entry.grid(row=1, column=1)

# button for capturing image
capture_button = ttk.Button(root, text="Capture Image", command=capture_image)
capture_button.grid(row=2, column=0, pady=10)

# button for marking attendance
mark_attendance_button = ttk.Button(root, text="Mark Attendance", command=mark_attendance)
mark_attendance_button.grid(row=3, column=0, pady=10)

image_label = ttk.Label(root)
image_label.grid(row=4, column=0, columnspan=2)

# Run the Tkinter main loop
root.mainloop()
