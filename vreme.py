import requests
import json
API_KEY="55811efe6c6e17339aa04dcc9f3c3bb5"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"
city=input("INTRODU NUMELE ORASULUI ")
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
rasp=requests.get(request_url)
data=json.loads(rasp.text)
print(data['wind']['speed'])
print(data['wind']['deg'])
# if rasp.status_code == 200:
#     data=rasp.json()
#     vremea=data['weather'][0]['description']
#     temp=round(data["main"]["temp"] -273.15,2)
#     print("Vremea", vremea)
#     print("temperatura: ", temp , " C")
#     wind=round(data["wind"]["speed"])
#     deg=round(data["wind"]["deg"])
#     print("vant: ", wind," ",deg)
    
# else:
#     print("avem o eroare :|")
