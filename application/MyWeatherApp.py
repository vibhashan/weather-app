"""
My custom weather app
Displays current weather conditions for particular city/region
"""
from tkinter import *
from tkinter import messagebox
import requests
import json

root = Tk()
root.title("Weather App")

root_window_width = 400
root_window_height = 400

# get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - root_window_width / 2)
center_y = int(screen_height/2 - root_window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{root_window_width}x{root_window_height}+{center_x}+{center_y}')

heading = Label(root, text="WEATHERY", font=("Poppins", 20), fg="blue")
heading.place(anchor=CENTER, relx=.5, rely=.05)

my_label = Label(root, text="City name", font=("Helvetica", 12))
my_label.place(anchor=CENTER, relx=0.25, rely=0.2)

input_box = Entry(root, width=25)
input_box.place(anchor=CENTER, relx=0.6, rely=0.2)

# define find() function
def find():
    entry_value = input_box.get()

    if entry_value == "":
        messagebox.showerror("Error", "Input field is empty!")

    else:
        api_url_location = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=%09yEVjxqdV1h2Uai7ocRGBixSqD5qTMR0k&q=" + entry_value

        try:
            api_location_request = requests.get(api_url_location)
            api_location_data = json.loads(api_location_request.content)

            location_key = api_location_data[0]["Key"]
            city_name = api_location_data[0]["LocalizedName"]
            admin_area = api_location_data[0]["AdministrativeArea"]["LocalizedName"] + " " + api_location_data[0]["AdministrativeArea"]["LocalizedType"]
            latitude = str(api_location_data[0]["GeoPosition"]["Latitude"])
            longitude = str(api_location_data[0]["GeoPosition"]["Longitude"])


            # api url for current weather conditions
            api_url_weather = "http://dataservice.accuweather.com/currentconditions/v1/" + location_key +"?apikey=%09yEVjxqdV1h2Uai7ocRGBixSqD5qTMR0k&details=true"

            try:
                api_weather_request = requests.get(api_url_weather)
                api_weather_data = json.loads(api_weather_request.content)

                observ_time_local = api_weather_data[0]["LocalObservationDateTime"]
                weather_status = api_weather_data[0]["WeatherText"]
                is_day_time = api_weather_data[0]["IsDayTime"]
                temperature = str(api_weather_data[0]["Temperature"]["Metric"]["Value"]) + " " + api_weather_data[0]["Temperature"]["Metric"]["Unit"]
                feeling_temp = str(api_weather_data[0]["RealFeelTemperature"]["Metric"]["Value"]) + " " + api_weather_data[0]["RealFeelTemperature"]["Metric"]["Unit"]
                feeling_phrase = api_weather_data[0]["RealFeelTemperature"]["Metric"]["Phrase"]
                relative_humidity = str(api_weather_data[0]["RelativeHumidity"])
                wind = str(api_weather_data[0]["Wind"]["Speed"]["Metric"]["Value"]) + " " + api_weather_data[0]["Wind"]["Speed"]["Metric"]["Unit"] + " " +api_weather_data[0]["Wind"]["Direction"]["English"]
                pressure = str(api_weather_data[0]["Pressure"]["Metric"]["Value"]) + " " + api_weather_data[0]["Pressure"]["Metric"]["Unit"] + ", " + api_weather_data[0][ "PressureTendency"]["LocalizedText"]

                details = Label(root, text="City : " + city_name + "\nAdministration Area : " + admin_area + "\n" +
                                "Latitude : " + latitude + "\nLongitude : " + longitude + "\n\n" +

                                "Observation time : " + observ_time_local + "\nWeather Status : " + weather_status +
                                "\nIs day time : " + str(is_day_time) + "\nTemperature : " + temperature + "\n" +
                                "Feeling temperature : " + feeling_temp + "\nFeeling : " + feeling_phrase + "\n" +
                                "Relative humidity : " + relative_humidity + "\nWind : " + wind + "\n" +
                                "Pressure : " + pressure)

                details.place(anchor="center", rely=0.65, relx=0.5)

            except Exception as e1:
                print(e1)

                if e1 == 0:
                    messagebox.showerror("Error", "API service currently unavailable!")

                else:
                    messagebox.showinfo("No results", "No results found!")

        except Exception as e:
            print(e)
            if e == 0:
                messagebox.showerror("Error", "API service currently unavailable!")

            else:
                messagebox.showinfo("Info", "No results found!\nMake sure that the spellings are correct")


find_button = Button(root, text="FIND", borderwidth=3, width=10, padx=2, pady=2, command=find)
find_button.place(anchor=CENTER, rely=0.3, relx=0.5)


root.mainloop()
