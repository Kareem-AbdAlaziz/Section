from tkinter import *
import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_sound():
    text = ueser_input.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text, lang='en')
            tts.save("audio.mp3")
            os.system("start audio.mp3" if os.name == "nt" else "open audio.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "No text found,Try again.")

def Set_text():
    ueser_input.delete("1.0", tk.END)

def Exit_app():
    app.destroy()

# Create the main window
app = tk.Tk()
app.title("GUI:Text to speech")
app.resizable(False,False)
app.geometry("800x400")
app.configure(bg="#0d3d99")

icno=PhotoImage(file="wave-sound.png")

app.iconphoto(False,icno)

Frame1=Frame(app,bg="white",width=800,height=65).place(x=0,y=0)

top_text=Label(app,text="Text to Speech GUI",font="Lato 20 bold",bg="white").place(x=260,y=20)

# Create a text entry widget
ueser_input = tk.Text(app, wrap=tk.WORD, height=10, width=50)
ueser_input.pack(pady=10)
ueser_input.place(x=200,y=80)
#text_entry.place(x=200,y=280)

# Create buttons
Launch_sound = tk.Button(app, text="Play", font="arial 15 bold",bg="green",command=play_sound)
Launch_sound.pack(pady=10)
Launch_sound.place(x=200,y=280)

Restart = tk.Button(app, text="Set", font="arial 15 bold",bg="red",command=Set_text)
Restart.pack(pady=10)
Restart.place(x=370,y=280)

Exit = tk.Button(app, text="Exit", font="arial 15 bold",bg="yellow",command=Exit_app)
Exit.pack(pady=10)
Exit.place(x=550,y=280)

# Run the application
app.mainloop()