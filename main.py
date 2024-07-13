import requests
from twilio.rest import Client # type: ignore

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"
api_key = "d4e468ed765e526c8b41e3bb1b7ad6ae"

account_sid = "ACdslsdflhdshlsdhi3wi3ih3i3"
auth_token = "GF5sjoeodepdldpdodopwpe4pepe"

weather_params = {
    "lat": 43.044392,
    "lon": 16.08950,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body = "It's going to rain today. Remember to bring an umbrella.",
        from_ ="+12057362627",
        to = "Your verified number"
    )
    #print("Bring an umbrella.")
    print(message.status)