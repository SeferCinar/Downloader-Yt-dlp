import tkinter as tk
import random
import subprocess
window = tk.Tk()
window.geometry("300x150")
window.title("Downloader App")
var = tk.StringVar(value=" ")
selectionText = tk.Label(
    text="Please select",
    width=30
    )
def getVideo():
    url = link.get()
    selection = var.get()
    if selection == "Audio":
        subprocess.run(["yt-dlp","-x",f"{url}","--restrict-filenames"])
    else:
        subprocess.run(["yt-dlp",f"{url}","--restrict-filenames"])
    
def selection():
    selection = var.get()

    
    selectionText.config(text=selection)
frame = tk.Frame()
R1 = tk.Radiobutton( master=frame,text="Audio",
                    value="Audio",  
                    command=selection,
                    variable=var)  
R1.pack()  
  
R2 = tk.Radiobutton( master=frame,text="Video",
                    value="Video",  
                   command=selection,
                   variable=var)  
R2.pack( )     

button = tk.Button(
    text="Download",
    width=10,
    height=1,
    bg="gray",
    fg="black",
    activebackground="yellow",
    command=getVideo
    )
link = tk.Entry()
link.pack()
frame.pack()
selectionText.pack()
button.pack()

window.mainloop()