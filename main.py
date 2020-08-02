import tkinter as tk
import tkinter.filedialog as tkFileDialog
import better_tkinter as btk
import json
import requests
import yt_mp3
import threading


class Main(tk.Tk):
    def __init__(self):
        self.config_file = 'config.json'
        self.cfg = self.load_config(self.config_file)
        tk.Tk.__init__(self)
        tk.Tk.wm_geometry(self, '1280x720')
        tk.Tk.wm_title(self, 'YouTube MP3 Downloader')
        tk.Tk.config(self, bg = self.cfg['background'])
        tk.Tk.minsize(self, self.cfg['min_width'], self.cfg['min_height'])
        
        self.load_images()
        self.current_frame = None
        self.switch_frame(Menu)
            
    
    def switch_frame(self, frame):
        for widget in self.winfo_children():
            widget.destroy()
        self.current_frame = frame(self)
        self.current_frame.pack()

    def load_config(self, filename):
        _file = open(filename, 'r')
        text = _file.read()
        _file.close()
        return json.loads(text)

    def load_images(self):
        self.image_cache = {
            'neutral': tk.PhotoImage(file = 'button_states/neutral.png'),
            'hover': tk.PhotoImage(file = 'button_states/hover.png'),
            'clicked': tk.PhotoImage(file = 'button_states/clicked.png'),
            'neutral_mini': tk.PhotoImage(file = 'button_states/neutral_mini.png'),
            'hover_mini': tk.PhotoImage(file = 'button_states/hover_mini.png'),
            'clicked_mini': tk.PhotoImage(file = 'button_states/clicked_mini.png'),
        }



class Menu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg = master.cfg['background'])
        
        header = tk.Frame(self, bg = master.cfg['background'])
        header.pack(pady = 20)
        btk.Label(header, text = 'YouTube MP3 Downloader', fontsize = 30).pack()

        body1 = tk.Frame(self, bg = master.cfg['background'])
        body1.pack(pady = 40)
        btk.Label(body1, text = 'Enter song or playlist link').pack(pady = 5)
        self.link = btk.Entry(body1, width = 40)
        self.link.pack(pady = 5)

        body2 = tk.Frame(self, bg = master.cfg['background'])
        body2.pack(pady = 5)
        btk.Label(body2, text = 'Enter or Browse for output directory').pack(pady = 5)
        self.location = btk.Entry(body2, width = 35)
        self.location.pack(pady = 5, padx = 7, side = tk.LEFT)
        btk.MiniButton(body2, text = '📁', command = self.browse).pack(pady = 5, padx = 7, side = tk.RIGHT)

        body3 = tk.Frame(self, bg = master.cfg['background'])
        body3.pack(pady = 5)
        btk.Button(body3, text = 'Confirm', command = self.on_confirm).pack(pady = 20, side = tk.LEFT)


    def on_confirm(self):
        url = self.link.get()
        self.link.delete(0, tk.END)
        dir = self.location.get()
        
        # check if website exists
        try:
            request = requests.get(url)
        except requests.exceptions.MissingSchema:
            self.link.insert(0, 'Format must be https://www.youtube.com/...')
            return
        if request.status_code == 200:
            try:
                yt_mp3.download_playlist(url, dir)
            except KeyError:
                try:
                    yt_mp3.download_video(url, dir)
                except:
                    self.link.insert(0, 'Invalid YouTube playlist or video link')


    def browse(self):
        dir = tkFileDialog.askdirectory(title = "Select directory")
        self.location.delete(0, tk.END)
        self.location.insert(0, dir)

if __name__ == '__main__':
    Main().mainloop()