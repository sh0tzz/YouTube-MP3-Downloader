import tkinter as tk



class Button(tk.Button):
    def __init__(self, master, font = 'Arial', fontsize = '18', fontstyle = 'bold', images = None, bg = None, fg = None, **kwargs):
        if bg == None:
            bg = master.master.master.cfg['background']
        if fg == None:
            fg = master.master.master.cfg['button_foreground']
        if images == None:
            self.images = master.master.master.image_cache
        else:
            self.images = images

        font = (font, fontsize, fontstyle)
        super().__init__(master, font = font, image = self.images['neutral'], compound = tk.CENTER, bg = bg,
        fg = fg, borderwidth = 0, highlightthickness = 0, activebackground = bg, activeforeground = fg, **kwargs)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)
        self.bind('<ButtonRelease-1>', self.on_release)

    def on_enter(self, x):
        self.config(image = self.images['hover'])

    def on_leave(self, x):
        self.config(image = self.images['neutral'])

    def on_click(self, x):
        self.config(image = self.images['clicked'])

    def on_release(self, x):
        self.config(image = self.images['hover'])



class NoHoverButton(tk.Button):
    def __init__(self, master, font = 'Arial', fontsize = '18', fontstyle = 'bold', image = None, bg = None, fg = None, **kwargs):
        if bg == None:
            bg = master.master.master.cfg['background']
        if fg == None:
            fg = master.master.master.cfg['button_foreground']

        font = (font, fontsize, fontstyle)
        super().__init__(master, font = font, image = image, compound = tk.CENTER, bg = bg,
        fg = fg, borderwidth = 0, highlightthickness = 0, activebackground = bg, activeforeground = fg, **kwargs)



class MiniButton(tk.Button):
    def __init__(self, master, font = 'Arial', fontsize = '18', fontstyle = 'bold', images = None, bg = None, fg = None, **kwargs):
        if bg == None:
            bg = master.master.master.cfg['background']
        if fg == None:
            fg = master.master.master.cfg['button_foreground']
        if images == None:
            self.images = master.master.master.image_cache
        else:
            self.images = images

        font = (font, fontsize, fontstyle)
        super().__init__(master, font = font, image = self.images['neutral_mini'], compound = tk.CENTER, bg = bg,
        fg = fg, borderwidth = 0, highlightthickness = 0, activebackground = bg, activeforeground = fg, **kwargs)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)
        self.bind('<ButtonRelease-1>', self.on_release)

    def on_enter(self, x):
        self.config(image = self.images['hover_mini'])

    def on_leave(self, x):
        self.config(image = self.images['neutral_mini'])

    def on_click(self, x):
        self.config(image = self.images['clicked_mini'])

    def on_release(self, x):
        self.config(image = self.images['hover_mini'])



class Label(tk.Label):
    def __init__(self, master, font = 'Arial', fontsize = '20', fontstyle = 'bold', bg = None, fg = None, **kwargs):
        if bg == None:
            bg = master.master.master.cfg['background']
        if fg == None:
            fg = master.master.master.cfg['foreground']
        font = (font, fontsize, fontstyle)
        super().__init__(master, font = font, bg = bg, fg = fg, **kwargs)



class Entry(tk.Entry):
    def __init__(self, master, font = 'Arial', fontsize = '20', fontstyle = 'bold', bg = None, fg = None, width = 5, **kwargs):
        if bg == None:
            bg = master.master.master.cfg['entry_background']
        if fg == None:
            fg = master.master.master.cfg['entry_foreground']
        font = (font, fontsize, fontstyle)
        super().__init__(master, font = font, bg = bg, fg = fg, width = width, highlightthickness = 0, relief = tk.SOLID, borderwidth = 2, **kwargs)



class Dropdown(tk.OptionMenu):
    def __init__(self, master, variable, *value, font = 'Arial', fontsize = '18', fontstyle = 'bold', bg = None, fg = None, width = 10, **kwargs):
        if bg == None:
            bg = master.master.master.cfg['entry_background']
        if fg == None:
            fg = master.master.master.cfg['entry_foreground']
        font = (font, fontsize, fontstyle)
        super().__init__(master, variable, *value, **kwargs)
        self.config(bg = bg, fg = fg, font = font, relief = tk.SOLID, highlightthickness = 0,
        activebackground = bg, activeforeground = fg, width = width)