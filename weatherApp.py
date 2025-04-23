from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import *
import requests
from timezonefinder import TimezoneFinder
import pytz
from PIL import Image, ImageTk
import time


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("640x480")
        self.root.title("Weather App")
        self.root.resizable(False, False)

        # Load and display the background image
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((640,480), Image.Resampling.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = Label(self.root, image=self.photo_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #variables
        self.var_city=StringVar()
        self.var_txtCity=StringVar()
        self.var_latitude=StringVar()
        self.var_temp=StringVar()
        self.var_humidity=StringVar()
        self.var_wind=StringVar()
        self.var_location=StringVar()
        self.var_localtime=StringVar()
        
        
        


if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()
