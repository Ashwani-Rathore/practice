import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests
HEIGHT = 600
WIDTH = 700
def get_weather(region):
    weather_key = 'd6451bb628620c7de8a7aec56b15096f'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q': region,'units': 'metric'}
    response = requests.get(url,params = params)
    weather = response.json()
    label['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    image_icon(icon_name)

def format_response(weather):
    name =weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    return "City name = {}\nWeather Conditions = {}\nTemperature(C) = {}".format(name, desc, temp)
def image_icon(icon_name):
    size = int(lower_frame.winfo_height()*0.25)# how we define size with winfo_height funtion of lower_frame object
    img = ImageTk.PhotoImage(Image.open('./img/'+icon_name+'.png').resize((size, size)))
    weather_icons.delete('all')# what this delete do
    weather_icons.create_image(0,0, anchor='nw', image=img) #what this create_image do and why there are two zeroes in the arguments
    weather_icons.image = img# what is the work of this image attribute


root = tk.Tk()
canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

photo = Image.open("weather.jpg")# for loading imgae in formats which are not supported by tkinter
background_img = ImageTk.PhotoImage(photo)# for converting image into tkinter supported format
background_lbl = tk.Label(root, image = background_img)
background_lbl.place(relheight = 1, relwidth = 1)

upper_frame = tk.Frame(root,bg = '#02A6AE', bd = 4)
upper_frame.place(relx = .2, rely = .1, relwidth = .6, relheight = .1)

textbox = tk.Entry(upper_frame,bg  = 'white', font = ('Arial', 12))
textbox.place(relwidth = .45, relheight = 1)

button = tk.Button(upper_frame, bg = 'white', text = 'Check Weather', font = ('Arial', 12), command = lambda:get_weather(textbox.get()))
button.place(relwidth = .50, relheight = 1, relx = .50)

lower_frame = tk.Frame(root, bg = '#02A6AE', bd = 4)
lower_frame.place(relx = .2, rely = .25, relwidth = .6, relheight = .5)

label = tk.Label(lower_frame,font = ('Arial', 12),anchor = 'nw', justify = 'left', bg = 'white')
label.place(relwidth = 1, relheight = 1)

weather_icons= tk.Canvas(label, bg = 'white')
weather_icons.place(relx = .70, rely = 0, relwidth = .30, relheight = .30)

root.mainloop()
