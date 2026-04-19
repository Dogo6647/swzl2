from customtkinter import *
import libswzl2

def space(mstr, hgt):
    s = CTkFrame(mstr, width=0, height=hgt)
    s.pack(padx=0, pady=0)

def paragraph(mstr, txt):
    t = CTkLabel(mstr, text=txt, fg_color="transparent", font=consb)
    t.pack(padx=0, pady=5)

def geek():
    print('stop itching around')

def encode():
    confrom = convfrm.cget('text')
    conto = convto.cget('text')
    libswzl2.encode(image_path=confrom, output_path=conto)

def decode():
    confrom = convfrm.cget('text')
    conto = convto.cget('text')
    libswzl2.decode(swzl_path=confrom, output_path=conto)

def filf():
    convfrm.configure(text=filedialog.askopenfilename())

def filt():
    convto.configure(text=filedialog.asksaveasfilename())


# create root window
root = CTk()
root.title("swzlr-gui")
root.geometry('360x300')
root.minsize(270, 300)
root.maxsize(540, 405)
root.iconbitmap('swzlr.ico')

rad=5
cons=("Consolas", 14)
consb=("Consolas Bold", 16)
hclr1="orange"
hclr2="#c18634"
hclr3="#3a2200"

#title
title = CTkLabel(root, text="swzlr-gui", fg_color="transparent", font=("Consolas Bold", 40), text_color=hclr1)
title.pack(padx=20, pady=15)

#space

space(root, 10)

#frame
frame = CTkScrollableFrame(root, width=300, height=150, corner_radius=rad)
frame.pack(padx=20, pady=0)

#ui
space(frame, 10)
paragraph(frame, "Convert from")
convfrm = CTkLabel(frame, text='', corner_radius=rad, font=cons)
convfrm.pack(padx=20, pady=0)
convfrmb = CTkButton(frame, text='Select file', corner_radius=rad, font=cons, command=filf)
convfrmb.pack(padx=20, pady=0)
paragraph(frame, "Convert to")
convto = CTkLabel(frame, text='', corner_radius=rad, font=cons)
convto.pack(padx=20, pady=0)
convtob = CTkButton(frame, text='Select file', corner_radius=rad, font=cons, command=filt)
convtob.pack(padx=20, pady=0)
space(frame, 20)
geek1 = CTkButton(frame, text='Encode', command=encode, width=100, corner_radius=rad, font=cons, fg_color=hclr2, hover_color=hclr3)
geek1.pack(padx=20, pady=0)
space(frame, 10)
geek2 = CTkButton(frame, text='Decode', command=decode, width=100, corner_radius=rad, font=cons, fg_color=hclr2, hover_color=hclr3)
geek2.pack(padx=20, pady=0) 
space(frame, 10)

# Tkinter event loop
root.mainloop()
