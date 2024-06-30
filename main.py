# Florens project main code
# Created:     2024-01-21
# Modified:    2024-06-30 (last status: working fine)
# Author:      Kagan Dikmen

from geopy.geocoders import Nominatim
from src.plant import Plant
from src.soil_composition import SoilComposition
from src.soil_current import SoilCurrent

def idealConditions(lat, lon, plant):

    try:
        localSoil = SoilComposition(lat, lon)
        localSoil.soilType()
        localSoil.optimalMoisture()
    except:
        print("ERROR: Soilgrids REST API access unsuccessful due to previous errors.")

    p = Plant(plant)
    return [p.optimalTemperature()[0], p.optimalTemperature()[1], localSoil.optMoisture['0_5cm'][0], localSoil.optMoisture['0_5cm'][1]]
    
    # TEST:
    # return [p.optimalTemperature()[0], p.optimalTemperature()[1], 0.05, 0.55]

def checkCurrentConditions(idealCondList, tempData, moistData):
    numGoodTempData = 0
    numGoodMoistData = 0

    minTemp = idealCondList[0]
    maxTemp = idealCondList[1]
    minMoist = idealCondList[2]
    maxMoist = idealCondList[3]

    for temperature in tempData:
        if temperature < maxTemp and temperature > minTemp:
            numGoodTempData = numGoodTempData + 1

    for moisture in moistData:
        if moisture < maxMoist and moisture > minMoist:
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

    latitude = latlon.latitude
    longitude = latlon.longitude

    print(f"Coordinates: {latitude}  {longitude}")

    s = SoilCurrent(latitude, longitude)

    interpretcurrentconditions(checkCurrentConditions(idealConditions(latitude, longitude, PLANT), s.currentConditions()['tempData'], s.currentConditions()['moistData']))

main()