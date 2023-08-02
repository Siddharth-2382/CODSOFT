from tkinter import *

# Constant for theme color of Weather Forecasting App
THEME_COLOR = "#d6f1ff"
FONT_NAME = "Courier"


def forecast():
    pass


window = Tk()
window.title("Weather Forecaster")
window.config(padx=20, pady=20, bg=THEME_COLOR)

# Label for app name
title_label = Label(text="Weather Forecaster", bg=THEME_COLOR, fg="#16018a", font=(FONT_NAME, 50))
title_label.pack(pady=15)

# Label for asking city name
city_name_label = Label(text="Enter your city's name:", bg=THEME_COLOR, fg="#16018a", font=(FONT_NAME, 20))
city_name_label.place(x=10, y=100)

# Entry field for city name
city_name_entry = Entry(fg="#16018a", width=15, font=(FONT_NAME, 20))
city_name_entry.place(x=300, y=100)

# Button for getting weather forecast
get_weather_button = Button(text="Get Weather", fg="#16018a", font=(FONT_NAME, 20), command=forecast)
get_weather_button.place(x=190, y=150)

# Label for weather description
description_label = Label(text="Description:", bg=THEME_COLOR, fg="#16018a", font=(FONT_NAME, 20))
description_label.place(x=10, y=225)

# Label for displaying weather description
description_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
description_display.place(x=200, y=225)

# Label for temperature
temperature_img = PhotoImage(file="images/temperature.png")
temperature_label = Label(image=temperature_img, bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
temperature_label.place(x=10, y=275)

# Label for displaying temperature
temperature_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
temperature_display.place(x=35, y=375)

# Label for windspeed
windspeed_img = PhotoImage(file="images/windspeed.png")
windspeed_label = Label(image=windspeed_img, bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
windspeed_label.place(x=220, y=275)

# Label for displaying windspeed
windspeed_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
windspeed_display.place(x=255, y=375)

# Label for humidity
humidity_img = PhotoImage(file="images/humidity.png")
humidity_label = Label(image=humidity_img, bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
humidity_label.place(x=430, y=275)

# Label for displaying humidity
humidity_display = Label(text="", bg=THEME_COLOR, fg="#db886a", font=(FONT_NAME, 20))
humidity_display.place(x=465, y=375)

# Window configuration
window.geometry("+450+125")
window.minsize(width=270, height=500)
window.resizable(False, False)
window.mainloop()
