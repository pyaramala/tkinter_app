import tkinter as tk
import threading
import flask
from flask import Flask,jsonify
from tkinter import messagebox
import time
def create_tkinter_window():
    def on_submit():
        messagebox.showinfo("Info", "Button Clicked!")

    root = tk.Tk()
    root.title("Simple Tkinter window!")
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    label = tk.Label(frame, text="Hello tkinter!")
    label.pack(padx=10,pady=10)
    button = tk.Button(frame,text = "Click me",command=on_submit)
    button.pack(padx=10,pady=10)
    root.mainloop()


def open_window():
    
    thread = threading.Thread(target=create_tkinter_window)
    
    thread.start()
    time.sleep(1)
    return jsonify({"status":"success","message": "tkinter window opened"})

app = Flask(__name__)
app.add_url_rule('/','window',open_window)


if __name__=="__main__":
    app.run(debug=True)