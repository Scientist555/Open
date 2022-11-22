import requests

city = "Moscow, RU"
appid = "134aacc1a016d54b0330e41bc4b9db51"
resOnToDay = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru','APPID': appid,})
dataOnToday = resOnToDay.json()
vidimost = dataOnToday['visibility']/1000
print("_______________________________________")
print("Прогноз погоды на день")
print("Город:", city)
print("Погодные условия:", dataOnToday['weather'][0]['description'])
print("Температура:", dataOnToday['main']['temp'])
print("Минимальная температура:", dataOnToday['main']['temp_min'])
print("Максимальная температура", dataOnToday['main']['temp_max'])
print("Скорость ветра: ", dataOnToday['wind']['speed'], " м/с ")
print("Видимость: ",vidimost, " км ")
print("_______________________________________")
print("Прогноз погоды на неделю")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city,'units':'metric','lang':'ru','APPID': appid})
dataWeek = res.json()
for i in dataWeek['list']:
    vidimostlong = i['visibility']/1000
    print("_______________________________________")
    print("Дата <", i['dt_txt'],">\r\nТемпература <",
    '{0:+1.0f}'.format(i['main']['temp']),">\r\nПогодные условия <",i['weather'][0]['description'],">")
    print("Скорость ветра: ", i['wind']['speed'], " м/с ")
    print("Видимость: ",vidimostlong, " км ")
    print("_______________________________________")
    