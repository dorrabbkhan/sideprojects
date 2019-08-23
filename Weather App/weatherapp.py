"""
Simple weather application built in Tkinter
"""


import tkinter as tk
import requests
from tkinter import font


HEIGHT = 400
WIDTH = 500
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
    populate_labels(weather)
    # parse the response and populate labels


def populate_labels(weather):
    """
    Extract values from JSON and put into the output labels
    """

    try:
        place_name = weather['name']
        description = weather['weather'][0]['description'].title()
        temp = weather['main']['temp']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        min_temp = weather['main']['temp_min']
        max_temp = weather['main']['temp_max']
        visibility = weather['visibility']
        # extract all values

    except:
        lower_label_two['text'] = "Error retrieving information"
        # display error message

    else:
        city_label['text'] = place_name
        temp_label['text'] = str(temp) + " °C"
        desc_label['text'] = description
        lower_label_one['text'] = f'Humiditiy: {humidity} %   Min: {min_temp} °C    Max: {max_temp} °C'
        lower_label_two['text'] = f"Pressure: {pressure} mb     Visibility: {visibility}m"
        # populate the label


root = tk.Tk()
root.resizable(0, 0)
# create root and canvas

frame = tk.Frame(root, bg='#4f8eb0', bd=20, height=HEIGHT, width=WIDTH)
frame.pack()
# create main frame

city_label = tk.Label(frame, bg='#4f8eb0', font=('Segoe UI', 20))
city_label.place(relx=0, rely=0.1, relwidth=1, relheight=0.25)

temp_label = tk.Label(frame, bg='#4f8eb0', font=('Segoe UI', 90))
temp_label.place(relx=0, rely=0.3, relwidth=1, relheight=0.3)

desc_label = tk.Label(frame, bg='#4f8eb0', font=('Segoe UI', 30))
desc_label.place(relx=0, rely=0.6, relwidth=1, relheight=0.3)

lower_label_one = tk.Label(frame, bg='#4f8eb0', font=('Segoe UI', 15))
lower_label_one.place(relx=0, rely=0.85, relwidth=1, relheight=0.075)

lower_label_two = tk.Label(frame, bg='#4f8eb0', font=('Segoe UI', 15))
lower_label_two.place(relx=0, rely=0.925, relwidth=1, relheight=0.075)

entry = tk.Entry(frame, bg='white')
entry.place(relx=0, rely=0, relwidth=0.8, relheight=0.1)

button = tk.Button(frame, text="Get weather", bg='white',
                   fg='black', command=lambda: get_weather(entry.get()))
button.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)
# create labels, entry and button

root.mainloop()
# make window
