import tkinter as tk
import random
import subprocess
window = tk.Tk()
def getVideo():
    url = link.get()
    subprocess.run(["yt-dlp",f"{url}","--restrict-filenames"])

    
greeting = tk.Label(
    text="Link",
    width=30
    )
button = tk.Button(
    text="Download",
    width=10,
    height=1,
    bg="yellow",
    fg="black",
    command=getVideo
    )
link = tk.Entry()
link.pack()
greeting.pack()
button.pack()
window.mainloop()