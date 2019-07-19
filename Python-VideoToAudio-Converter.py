# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO CONVERT A VIDEO FILE INTO AN AUDIO FILE

# The Conversion Of Video File Into An Audio Can Be Done With The Help Of
# moviepy Module Of Python. The Module Can Be Installed using The Command
# pip install moviepy

# Importing necessary packages
import tkinter as tk
import moviepy.editor as audcon
from tkinter import *
from tkinter import messagebox, filedialog

#---

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreatWidgets():
    sourceLabel = Label(root, text="VIDEO PATH : ",
                        bg="steelblue", font=('Helvetica', 10, 'bold'))
    sourceLabel.grid(row=1, column=1, padx=5, pady=20)

    root.sourceEntry = Entry(root, width=35, textvariable=source)
    root.sourceEntry.grid(row=1, column=2, padx=5, pady=20)

    destinationLabel = Label(root, text="AUDIO PATH : ",
                             bg="steelblue", font=('Helvetica', 10, 'bold'))
    destinationLabel.grid(row=3, column=1, padx=5, pady=20)

    root.destinationEntry = Entry(root, width=35, textvariable=destination)
    root.destinationEntry.grid(row=3, column=2, padx=5, pady=20)

    SRCBrowseBTN = Button(root, text="BROWSE", command=SBrowse, width=10)
    SRCBrowseBTN.grid(row=1, column=3, padx=5, pady=20)

    DESTBrowseBTN = Button(root, text="BROWSE", command=DBrowse, width=10)
    DESTBrowseBTN.grid(row=3, column=3, padx=5, pady=20)

    convertBTN = Button(root, text="CONVERT VIDEO", command=Convert, width=35)
    convertBTN.grid(row=2, column=1,columnspan = 3, padx=5, pady=5)

#---

# Defining Browse() to select the video file to be converted to audio file
def SBrowse():
    # Retrieving the user-input video file name
    videoName = filedialog.askopenfilename(initialdir="C:\Python\PyVideo2Audio",
                                           filetypes = (("MP4 (*.mp4)","*.mp4"),
                                                        ("AVI (*.avi", "*.avi"),
                                                        ("All File")))
    # Displaying the video file name in the sourceEntry Box
    root.sourceEntry.insert(0, videoName)


# Defining Browse() to select a destination folder to save the audio file
def DBrowse():
    # Retrieving the user-input audi file name
    audioName = filedialog.asksaveasfilename(initialdir="C:\Python\PyVideo2Audio",
                                             defaultextension=".mp3",
                                             filetypes = (("MP3 (*.mp3)","*.mp3"),
                                                        ("WAV (*.wav", "*.wav"),
                                                        ("All File")))
    # Displaying the audio file name in the destinationEntry Box
    root.destinationEntry.insert(0, audioName)

#---

# Defining the Convert() to convert the video file to an audio file
def Convert():
    # Retrieving and storing user-input video and audio filenames
    sourceFile = source.get()
    destinationFile = destination.get()

    # Loading the video clip
    sourceVideo = audcon.VideoFileClip(sourceFile)

    # Converting and saving the video file to audio file.
    sourceVideo.audio.write_audiofile(destinationFile)

    messagebox.showinfo("SUCCESS", "VIDEO CONVERTED SUCCESSFULLY")

#---

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window and
# disabling the resizing property
root.title("PyVideo2Audio")
root.config(bg="steelblue")
root.geometry("440x170")
root.resizable(False, False)

# Creating tkinter variable
source = StringVar()
destination = StringVar()

# Calling the CreateWidgets() function
CreatWidgets()

# Defining infinite loop to run application
root.mainloop()

#---