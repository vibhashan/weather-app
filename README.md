# weather-app

# Description
A simple weather app developed using Python Tkinter library and AccuWeather API. This project is solely targetted for newbies getting started with
Python GUI development and using APIs with Python. The application has minimum styling and focuses more on API usage and GUI development.
A user can simply enter a city and get the weather details as illustrated in the figure below.


<p align="center">
  Figure 1 <br />
  <img src="https://github.com/vibhashan/weather-app/assets/137031728/be49292c-1844-40c0-8648-baddc9157d84" width="300" height="300">
</p> 

# 🔥 Getting Started
1. Download or clone the repository using "git clone https://github.com/vibhashan/weather-app.git"
2. Navigate to "weather-app/application" and run the "MyWeatherApp.py" file to open the GUI interface.

# 😢 Limitations
The application uses a free API account from AccuWeather APIs website. So, there is only a limited no.of API requests per day.
However you can simply create a free API account from "https://developer.accuweather.com/" and paste the account key in the following places :
- Line no 44 --> api_url_location = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=<your_api_key>=" + entry_value
- Line no 58 --> api_url_weather = "http://dataservice.accuweather.com/currentconditions/v1/" + location_key +"?apikey=<your_api_key>&details=true"

<br />

<p> Play around with the application and modify it as you need to be familiar with Tkinter GUI and API usage with Python. </p>
<p> Feel free to shary any suggestions as well 👍 </p> 

