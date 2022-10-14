# must uncomment this for mail to work
# import smtplib

import requests
from datetime import *

MY_LAT = 47.6062
MY_LON = -122.3321
tom = requests.get(url="http://api.open-notify.org/iss-now.json")
tom.raise_for_status()


data = tom.json()
lat = float(data["iss_position"]["latitude"])
long = float(data["iss_position"]["longitude"])

location = (long, lat)


def is_overhead():
    """is the iss overhead?"""
    if lat-5 <= MY_LAT <= lat+5:
        return True
    else:
        return False


def is_night():
    """is it night ouitside?"""
    if sunrise <= time_now.hour <= sunset:
        return False
    else:
        return True


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
solar_data = response.json()
sunrise = int(solar_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(solar_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def test():
    if is_overhead() and is_night():
        return True
    else:
        return False


# must add real info for email to work
MY_EMAIL = ""
MY_PW = ""
# assignment was to sent email, but i'm not making a fake email account to do this. its very easy to do
if test():
    print("Yay! Go outside and look for the ISS")
    # connection = smtplib.SMTP("smtp.gmail.com")
    # connection.starttls()
    # connection.login(MY_EMAIL, MY_PW)
    # connection.sendmail(
    #     from_addr=MY_EMAIL,
    #     to_addrs=MY_EMAIL,
    #     msg="Subject:Look up!\n\nThe ISS is above you in the sky!"
    # )
else:
    print("No! Stay indoors and watch more cartoons")

