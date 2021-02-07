import eel
import pyowm

@eel.expose
def get_weather(place):
    city = "New York, USA"

    owm = pyowm.OWM("4615727cb0b8911adac93dc624a4278c")
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "Temperature in " + city + " is now " + str(temp)
eel.init("web")
eel.start("main.html", size = (500, 500))