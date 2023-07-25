import json
import urllib.request


def weather_api():
    with urllib.request.urlopen(
            "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22") as url:
        data = json.load(url)
        print(data)
        print(data["cod"])
        get_user_input(data)


def get_weather_data(data):
    user_input_date = get_date_string()
    for weather_data in data["list"]:
        date_str = weather_data["dt_txt"]
        if user_input_date == date_str:
            weather = weather_data["main"]["temp"]
            print("Weather is  ({}) for the date ({})".format(weather,date_str ))
            return

    print("No weather data found for data: ({})".format(user_input_date))


def get_wind_speed_data(data):
    user_input_date = get_date_string()
    for weather_data in data["list"]:
        date_str = weather_data["dt_txt"]
        if user_input_date == date_str:
            speed = weather_data["wind"]["speed"]
            print("Wind speed is  ({}) for the date ({})".format(speed, date_str))
            return
    print("No Wind speed data found for data: ({})".format(user_input_date))


def get_pressure_data(data):
    user_input_date = get_date_string()
    for weather_data in data["list"]:
        date_str = weather_data["dt_txt"]
        if user_input_date == date_str:
            pressure = weather_data["main"]["pressure"]
            print("Pressure is  ({}) for the date ({})".format(pressure, date_str))
            return
    print("No Wind speed data found for data: ({})".format(user_input_date))


def get_date_string():
    return input("input date formate YYY-MM-dd hh:mm:ss . Eg: 2019-03-28 18:00:00 : ").strip()


def get_user_input(data):
    user_input = 2
    while user_input != "0":
        print("\n Hey user below are list options available")
        print(" 1. Get weather \n 2. Get Wind Speed \n 3. Get Pressure \n 0. Exit \n ")
        user_input = input("Enter your option : ").strip()
        if user_input == "1":
            get_weather_data(data)
        elif user_input == "2":
            get_wind_speed_data(data)
        elif user_input == "3":
            get_pressure_data(data)
        elif user_input == "0":
            continue
        else:
            print("\n your chosen wrong option  ")
    print("\n thanks you for . Good bye")



if __name__ == '__main__':
    weather_api()