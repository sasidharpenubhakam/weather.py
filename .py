import tkinter as tk
import requests

def fetch_weather():
    api_key = "74c5b073622bfb01e005f3d5b09b0c85" 
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        weather_description = weather_data["weather"][0]["description"].capitalize()
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_label.config(text=f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    else:
        weather_label.config(text="City not found")


root = tk.Tk()
root.title("Weather App")


city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text=" weather report ", command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()


root.mainloop()
