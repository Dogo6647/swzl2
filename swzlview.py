from tkinter import *
from sys import argv as arg
from os import system, name
import libswzl2
ip=(arg[1].replace("\\", "/")).split('/')[-1]
libswzl2.decode(swzl_path=ip, output_path=f"temp.{ip}.png")
root = Tk()
root.configure(background='black')
root.title(ip)
image = PhotoImage(file=f"temp.{ip}.png")
i = Label(root, image=image)
i.pack()
root.resizable(False, False)
print(ip)
root.mainloop()
system(f'{'del' if name=='nt' else 'rm'} temp.{ip}.png')