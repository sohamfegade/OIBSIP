import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

def fetch_weather():
    try:
        api_key = "26bc0127c8123c4f837770679512255a"  # Replace with your OpenWeatherMap API key
        city = city_entry.get()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Extracting weather information
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        # Displaying weather information
        temperature_label.config(text=f"Temperature: {temperature}°C")
        weather_desc_label.config(text=f"Weather: {weather_desc}")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")

        # Displaying weather icon
        icon_image = Image.open(r"C:\Users\soham\OneDrive\Desktop\OIBSIP\Weather app\Weather app.py").resize((80, 80))
        icon_photo = ImageTk.PhotoImage(icon_image)
        weather_icon_label.config(image=icon_photo)
        weather_icon_label.image = icon_photo
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")

# Creating the main window
root = tk.Tk()
root.title("Weather App")

# City entry
city_label = tk.Label(root, text="Enter City:")
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Fetch weather button
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

# Weather information labels
temperature_label = tk.Label(root, text="")
temperature_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
weather_desc_label = tk.Label(root, text="")
weather_desc_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
wind_speed_label = tk.Label(root, text="")
wind_speed_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Weather icon label
weather_icon_label = tk.Label(root)
weather_icon_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# Running the main event loop
root.mainloop()