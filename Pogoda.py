import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")

place = input('Где ты живёшь?:')

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature("celsius")["temp"]

print( "В городе " + place + " Температура около " + str(temp))