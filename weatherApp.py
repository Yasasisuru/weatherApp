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
        self.bg_image = self.bg_image.resize((700,480), Image.Resampling.LANCZOS)
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
        
        
        #----------data----------------
        self.var_txtCity=Label(self.root,text="city",font=("times 16 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_txtCity.place(x=230,y=200)
        self.var_latitude=Label(self.root,text="latitude",font=("times 10 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_latitude.place(x=230,y=250)
        self.var_temp=Label(self.root,text="temp",font=("times 60 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_temp.place(x=230,y=100)
        self.var_location=Label(self.root,text="location",font=("times 10 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_location.place(x=230,y=280)
        
        
        self.var_humidity=Label(self.root,text="hu",font=("times 14 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_humidity.place(x=500,y=430)
        self.var_wind=Label(self.root,text="wi",font=("times 14 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_wind.place(x=300,y=430)
        self.var_localtime=Label(self.root,text="ti",font=("times 14 bold"),fg='black',bg='#08f7f7',justify=CENTER)
        self.var_localtime.place(x=100,y=430)
        
        
        #label
        
        LabelHumidity=Label(self.root,text="Humidity",font=("times 10 bold")).place(x=500,y=400)
        LabelLocaltime=Label(self.root,text="Time",font=("times 10 bold")).place(x=300,y=400)
        LabelWind=Label(self.root,text="Wind",font=("times 10 bold") ).place(x=100,y=400)
        


if __name__ == "__main__":
    root = Tk()
    app = WeatherApp(root)
    root.mainloop()
