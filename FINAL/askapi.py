import requests
import json

def setcolor(value: int) -> str:

    # From https://www.airnow.gov/aqi/aqi-basics/

    if value > 0 and value < 50:

        return "green"

    elif value > 50 and value < 100:
        return "yellow"

    elif value > 100 and value < 150:
        return "orange"

    elif value > 150 and value < 200:
        return "red"

    elif value > 200 and value < 300:
        return "purple"

    elif value > 300:
        return "maroon"

    else:
        return "black"


def ask_air(city: str, apikey: str) -> dict:

    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': apikey})

    if response.status_code == requests.codes.ok:
    
        data = json.loads(response.text)

        for k,v in data.items():

            if isinstance(v, dict):
                
                v['color'] = setcolor(v["aqi"])

            else:

                aqi = v
                data[k] = {
                
                    "aqi":      aqi,
                    "color":    setcolor(aqi)
                
                }



        return data

    else:
        return {
                    'error': True,
                    'status_code': response.status_code,
                    'text': response.text
                }

def ask_weather(city: str, apikey: str) -> dict:

    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': apikey})

    if response.status_code == requests.codes.ok:
        
        data = json.loads(response.text)

        cloud = data['cloud_pct']

        if cloud >= 0 and cloud < 25:
            
            data['cloud_picture'] = "cloud0"

        elif cloud >= 25 and cloud < 75:

            data['cloud_picture'] = "cloud50"

        elif cloud >= 75 and cloud <= 100:
    
            data['cloud_picture'] = "cloud100"


        return data


    else:
        return {
                    'error': True,
                    'status_code': response.status_code,
                    'text': response.text
                }

