from customStyle import TextLike
from tkmacosx import Button
from tkinter import font as ft
import tkinter as tk

style1 = TextLike()

class TextLikeButton(tk.Label):
    def __init__(self, master=None, cnf={}, command=None,**kw):
        bg = kw.pop('bg', style1.bg)
        fg = kw.pop('fg', style1.fg)
        font = kw.pop('font', style1.font)
        font_size = kw.pop('font_size', style1.font_size)
        slant = kw.pop('slant', 'italic')
        overeffect = kw.pop('overeffect', 'bigger')
        overcolor = kw.pop('overcolor', style1.color_d)

        tk.Label.__init__(self, master, cnf,
                          bg=bg,
                          fg=fg,
                          font=ft.Font(family=font, size=font_size, slant=slant),
                          **kw)


        font1 = ft.Font(family=font, size=font_size, slant=slant)
        font2 = ft.Font(family=font, size=font_size+5, weight='bold', slant=slant)

        if overeffect == 'bigger':
            self.bind("<Enter>", lambda event: self.configure(font=font2))
            self.bind("<Leave>", lambda event: self.configure(font=font1))

        elif overeffect == 'color':
            self.bind("<Enter>", lambda event: self.configure(fg=overcolor))
            self.bind("<Leave>", lambda event: self.configure(fg=fg))

        self.bind("<Button-1>", lambda event: self.on_click(command))

    def on_click(self, command):
        if command:
            command(self)




class myButton(Button):
    def __init__(self, master=None, cnf={},
                 font=style1.font,
                 font_size=style1.font_size,
                 text_style='italic',
                 bg=style1.bg, fg=style1.fg,
                 style=style1, **kw):
        Button.__init__(self, master,
                        cnf,
                        bg=bg,
                        fg=fg,
                        font=ft.Font(family=font, size=font_size, slant=text_style),
                        bd=4,
                        borderless=style.borderless,
                        activebackground=style.activebackground,
                        activeforeground=style.activeforeground,
                        highlightthickness=style.highlightthickness,
                        highlightbackground=style.highlightcolor,
                        bordercolor=style.color_d,
                        overrelief=style.overrelief,
                        relief=style.relief,
                        focusthickness=style.focusthickness,
                        highlightcolor=style.highlightcolor,
                        overforeground=style.overforeground,
                        **kw)