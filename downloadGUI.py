import tkinter as tk
import random
import subprocess
window = tk.Tk()
window.geometry("500x200")
window.title("Downloader App")
var = tk.StringVar(value="Video")
labelText = tk.StringVar(value="Please select")
statusText = tk.StringVar(value="")
linkText= tk.StringVar(value="")
selectionText = tk.Label(
    text="Please select",
    width=30,
    font=("sans",16),
    textvariable=labelText,
    ).grid(row=0,column=0)
staticmethod = tk.Label(
    textvariable=statusText,
    font="sans"
).grid(row=4,column=0)
def getVideo():
    if linkText.get() == "":
        statusText.set(value="Please enter a link")
    else:
        url = linkText.get()
        selection = var.get()
        if selection == "Audio":
            subprocess.run(["yt-dlp","-x",f"{url}","--restrict-filenames"])
        else:
            subprocess.run(["yt-dlp",f"{url}","--restrict-filenames"])  
    
    
def selection():
    selection = var.get() 
    labelText.set(selection)
    
frame = tk.Frame()
R1 = tk.Radiobutton( master=window,text="Audio",
                    value="Audio",  
                    command=selection,
                    variable=var,
                    border=5,
                    font="sans",
                    justify="left"
                    ).grid(row=1,column=1)
 
  
R2 = tk.Radiobutton( master=window,text="Video",
                    value="Video",  
                   command=selection,
                   font="sans",
                   justify="left",
                   variable=var).grid(row=2,column=1)
 

button = tk.Button(
    text="Download",
    width=10,
    height=1,
    bg="gray",
    fg="black",
    activebackground="yellow",
    highlightbackground="green",
    command=getVideo,
    font="sans",
    ).grid(row=2,column=0)
link = tk.Entry(
    font=("Helvetica", 12),
    textvariable=linkText
).grid(row=1,column=0)


window.mainloop()