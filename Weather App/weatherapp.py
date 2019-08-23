"""
Simple weather application built in Tkinter
"""

import tkinter as tk
import requests


HEIGHT = 400
WIDTH = 600
# set window width and height


def get_weather(city):
    """
    Get JSON data from Openweathermap API
    """

    api_key = '2e34849853646b75e5be71d39c1f90c3'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': api_key, 'q': city, 'units': 'metric'}
    # initialize API key, URL and parameters for request

    response = requests.get(url, params=params)
    weather = response.json()
    populate_label(weather)
    # parse the response and populate label


def populate_label(weather):
    """
    Extract values from JSON and put into the output label
    """
    
    place_name = weather['name']
    description = weather['weather'][0]['description'].title()
    temp = weather['main']['temp']
    pressure = weather['main']['pressure']
    humidity = weather['main']['humidity']
    min_temp = weather['main']['temp_min']
    max_temp = weather['main']['temp_max']
    wind = weather['wind']
    visibility = weather['visibility']
    # extract all values

    text = f"City: {place_name}\nDescription:{description}\nTemperature:{temp}"
    label['text'] = text
    # populate the label


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# create root and canvas

frame = tk.Frame(root, bg='blue')
frame.place(relwidth=1, relheight=1)
# create main frame

label = tk.Label(frame, text="This is a label", bg='gray')
label.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0, rely=0, relwidth=0.8, relheight=0.1)

button = tk.Button(root, text="Text Button", bg='black',
                   fg='white', bd=5, command=lambda: get_weather(entry.get()))
button.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)
# create label, entry and button

root.mainloop()
# make window
