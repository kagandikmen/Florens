# When-to-Plant project main code
# Created:     2024-01-21
# Modified:    2024-06-29 (last status: working fine)
# Author:      Kagan Dikmen

# import datetime
from geopy.geocoders import Nominatim
import requests
from soil import Soil

# TODO: all times are GMT for the time being, add the capability to display things in local time 
    # (don't know if I will use timestamps anywhere)
# TODO: add a SQL database for the plant data

BASE_URL = "https://api.open-meteo.com/v1/forecast?"

def idealConditions(lat, lon, plant):

    try:
        localSoil = Soil(lat, lon)
        localSoil.rawSoilData()
        localSoilType = localSoil.soilType()
        optMoist = localSoil.optimalMoisture(localSoilType)
    except:
        print("ERROR: Soilgrids REST API access unsuccessful due to previous errors.")

    match plant:
        case "tulip": return [4.5, 12, optMoist['0_5cm'][0], optMoist['0_5cm'][1]]
        case "wheat": return [12.5, 25, optMoist['0_5cm'][0], optMoist['0_5cm'][1]]    # https://www.canr.msu.edu/news/planting_wheat_into_dry_soil
        #case "test": return [-4, 45, 0.05, 0.50]  
        case _: return [100, 100, 1, 1]

def checkCurrentConditions(idealCondList, tempData, moistData):
    numGoodTempData = 0
    numGoodMoistData = 0

    for temperature in tempData:
        if temperature < idealCondList[1] and temperature > idealCondList[0]:
            numGoodTempData = numGoodTempData + 1

    for moisture in moistData:
        if moisture < idealCondList[3] and moisture > idealCondList[2] :
            numGoodMoistData = numGoodMoistData + 1

    return (numGoodTempData, numGoodMoistData)

def interpretcurrentconditions(resulttuple):
    tempcheckresult = resulttuple[0] > 168*0.75
    moistcheckresult = resulttuple[1] > 168*0.75

    print("Temperature check result: ", end='')
    if tempcheckresult:
        print("positive")
    else:
        print("negative")
        
    print("Moisture check result: ", end='')
    if moistcheckresult:
        print("positive")
    else:
        print("negative")

    print("The next 7 days are ", end='')
    if tempcheckresult and moistcheckresult:
        print("ideal ", end='')
    else:
        print("NOT ideal ", end='')
    print("for planting.")

def main():
    PLANT = input("What do you want to plant?\t").lower()

    CITY = input("Where do you want to plant?\t").lower()
    latlon = Nominatim(user_agent="Florens").geocode(CITY)

    latitude = latlon.latitude;         #float(input("Latitude: "))
    longitude = latlon.longitude;       #float(input("Longitude: "))

    print(f"Coordinates: {latitude}  {longitude}")

    URL_TEMPLATE = BASE_URL + "latitude=" + "%.2f" % latitude + "&longitude=" + "%.2f" % longitude

    URL_ST0     = URL_TEMPLATE + "&hourly=soil_temperature_0cm"
    URL_ST6     = URL_TEMPLATE + "&hourly=soil_temperature_6cm"
    URL_ST18    = URL_TEMPLATE + "&hourly=soil_temperature_18cm"
    URL_ST54    = URL_TEMPLATE + "&hourly=soil_temperature_54cm"

    URL_SM0_1   = URL_TEMPLATE + "&hourly=soil_moisture_0_to_1cm"
    URL_SM1_3   = URL_TEMPLATE + "&hourly=soil_moisture_1_to_3cm"
    URL_SM3_9   = URL_TEMPLATE + "&hourly=soil_moisture_3_to_9cm"
    URL_SM9_27  = URL_TEMPLATE + "&hourly=soil_moisture_9_to_27cm"
    URL_SM27_81 = URL_TEMPLATE + "&hourly=soil_moisture_27_to_81cm"

    response_st0        = requests.get(URL_ST0).json()
    response_st6        = requests.get(URL_ST6).json()
    response_st18       = requests.get(URL_ST18).json()
    response_st54       = requests.get(URL_ST54).json()

    response_sm0_1      = requests.get(URL_SM0_1).json()
    response_sm1_3      = requests.get(URL_SM1_3).json()
    response_sm3_9      = requests.get(URL_SM3_9).json()
    response_sm9_27     = requests.get(URL_SM9_27).json()
    response_sm27_81    = requests.get(URL_SM27_81).json()

    st0_timelist    = response_st0['hourly']['time']
    st0_vallist     = response_st0['hourly']['soil_temperature_0cm']
    st6_timelist    = response_st6['hourly']['time']
    st6_vallist     = response_st6['hourly']['soil_temperature_6cm']
    st18_timelist   = response_st18['hourly']['time']
    st18_vallist    = response_st18['hourly']['soil_temperature_18cm']
    st54_timelist   = response_st54['hourly']['time']
    st54_vallist    = response_st54['hourly']['soil_temperature_54cm']

    sm0_1_timelist      = response_sm0_1['hourly']['time']
    sm0_1_vallist       = response_sm0_1['hourly']['soil_moisture_0_to_1cm']
    sm1_3_timelist      = response_sm1_3['hourly']['time']
    sm1_3_vallist       = response_sm1_3['hourly']['soil_moisture_1_to_3cm']
    sm3_9_timelist      = response_sm3_9['hourly']['time']
    sm3_9_vallist       = response_sm3_9['hourly']['soil_moisture_3_to_9cm']
    sm9_27_timelist     = response_sm9_27['hourly']['time']
    sm9_27_vallist      = response_sm9_27['hourly']['soil_moisture_9_to_27cm']
    sm27_81_timelist    = response_sm27_81['hourly']['time']
    sm27_81_vallist     = response_sm27_81['hourly']['soil_moisture_27_to_81cm']


    interpretcurrentconditions(checkCurrentConditions(idealConditions(latitude, longitude, PLANT), st6_vallist, sm3_9_vallist))

main()