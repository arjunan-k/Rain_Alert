import requests
from twilio.rest import Client

account_sid = "Type it from the twilio API"
auth_token = "Type it from the twilio API"
api_key = "Type the API key from open weather map"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {"lat": "50.629021", "lon": "-96.212250", "appid": api_key, "exclude": "current,daily,minutely"}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
rain = False
for i in range(0, 13):
    code_id = weather_data["hourly"][i]["weather"][0]["id"]
    if code_id < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Bring Umbrella, It's going to rain ☂️.",
            from_='Type if from the twilio API',
            to='your desired verified number in the twilio API'
        )
    print(message.status)