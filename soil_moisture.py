# Code taking and interpreting soil data for a location
# Created:     2024-01-22
# Modified:    2024-01-22 (last status: unknown)
# Author:      Kagan Dikmen

import requests
# from geopy.geocoders import Nominatim
# import geopy.point

# TODO: implement it with classes (maybe?)
# TODO: think of a way of implementing the error message better

# LATITUDE = float(input("Latitude: "))
# LONGITUDE = float(input("Longitude: "))

# p = geopy.point.Point(LATITUDE, LONGITUDE)
# r = Nominatim(user_agent = "When-to-Plant").reverse(p)
# print("This lat-lon pair correspond to: " + str(r))

def latlon2rawsoildata(lat, lon):
    
    TEMPLATE_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"

    response = requests.get(TEMPLATE_URL).json()

    # print(TEMPLATE_URL)

    # print("-" * 20)
    # print("-" * 20)

    # print(response)

    # print("-" * 20)
    # print("-" * 20)

    clay_data = response['properties']['layers'][0]['depths']
    sand_data = response['properties']['layers'][1]['depths']
    silt_data = response['properties']['layers'][2]['depths']
    try: 
        clay_p_0_5cm = clay_data[0]['values']['Q0.5'] / 1000
        clay_p_5_15cm = clay_data[1]['values']['Q0.5'] / 1000
        clay_p_15_30cm = clay_data[2]['values']['Q0.5'] / 1000
    
        sand_p_0_5cm = sand_data[0]['values']['Q0.5'] / 1000
        sand_p_5_15cm = sand_data[1]['values']['Q0.5'] / 1000
        sand_p_15_30cm = sand_data[2]['values']['Q0.5'] / 1000
    
        silt_p_0_5cm = silt_data[0]['values']['Q0.5'] / 1000
        silt_p_5_15cm = silt_data[1]['values']['Q0.5'] / 1000
        silt_p_15_30cm = silt_data[2]['values']['Q0.5'] / 1000
    except:
        print("ERROR: There is no soil data for the given location. It may be in a residential area or a water body.")

    return {'clay': [clay_p_0_5cm, clay_p_5_15cm, clay_p_15_30cm], 
            'sand': [sand_p_0_5cm, sand_p_5_15cm, sand_p_15_30cm], 
            'silt': [silt_p_0_5cm, silt_p_5_15cm, silt_p_15_30cm]} 


def rawsoildata2soiltype(rsoildata):

    clay0_5 = rsoildata['clay'][0]
    clay5_15 = rsoildata['clay'][1]
    clay15_30 = rsoildata['clay'][2]

    sand0_5 = rsoildata['sand'][0]
    sand5_15 = rsoildata['sand'][1]
    sand15_30 = rsoildata['sand'][2]

    silt0_5 = rsoildata['silt'][0]
    silt5_15 = rsoildata['silt'][1]
    silt15_30 = rsoildata['silt'][2]

    layers = {}

    # print(clay0_5)
    # print(sand0_5)
    # print(silt0_5)

    # 0-5 cm
    if clay0_5 >= 0.4 and sand0_5 <= 0.45 and silt0_5 <= 0.4:
        layers['0_5cm'] = 'clay'
    elif clay0_5 >= 0.4 and silt0_5 >= 0.4:
        layers['0_5cm'] = 'silty clay'
    elif clay0_5 >= 0.35 and sand0_5 >= 0.45:
        layers['0_5cm'] = 'sandy clay'
    elif clay0_5 >= 0.2 and clay0_5 <= 0.35 and sand0_5 >= 0.45 and silt0_5 <= 0.275:
        layers['0_5cm'] = 'sandy clay loam'
    elif clay0_5 >= 0.275 and clay0_5 <= 0.4 and sand0_5 >= 0.2 and sand0_5 <= 0.45:
        layers['0_5cm'] = 'clay loam'
    elif clay0_5 >= 0.275 and clay0_5 <= 0.4 and sand0_5 <= 0.2:
        layers['0_5cm'] = 'silty clay loam'
    elif clay0_5 >= 0.075 and clay0_5 <= 0.275 and sand0_5 <= 0.525 and silt0_5 >= 0.275 and silt0_5 <= 0.5:
        layers['0_5cm'] = 'loam' 
    elif (clay0_5 <= 0.275 and clay0_5 >= 0.125 and silt0_5 >= 0.5) or (clay0_5 <= 0.125 and silt0_5 >= 0.5 and silt0_5 <= 0.8):
        layers['0_5cm'] = 'silt loam' 
    elif clay0_5 <= 0.125 and silt0_5 >= 0.8:
        layers['0_5cm'] = 'silt'
    elif sand0_5 >= 0.9:
        layers['0_5cm'] = 'sand'
    elif sand0_5 >= 0.8:
        layers['0_5cm'] = 'loamy sand'
    else:
        layers['0_5cm'] = 'sandy loam'

    # 5-15 cm
    if clay5_15 >= 0.4 and sand5_15 <= 0.45 and silt5_15 <= 0.4:
        layers['5_15cm'] = 'clay'
    elif clay5_15 >= 0.4 and silt5_15 >= 0.4:
        layers['5_15cm'] = 'silty clay'
    elif clay5_15 >= 0.35 and sand5_15 >= 0.45:
        layers['5_15cm'] = 'sandy clay'
    elif clay5_15 >= 0.2 and clay5_15 <= 0.35 and sand5_15 >= 0.45 and silt5_15 <= 0.275:
        layers['5_15cm'] = 'sandy clay loam'
    elif clay5_15 >= 0.275 and clay5_15 <= 0.4 and sand5_15 >= 0.2 and sand5_15 <= 0.45:
        layers['5_15cm'] = 'clay loam'
    elif clay5_15 >= 0.275 and clay5_15 <= 0.4 and sand5_15 <= 0.2:
        layers['5_15cm'] = 'silty clay loam'
    elif clay5_15 >= 0.075 and clay5_15 <= 0.275 and sand5_15 <= 0.525 and silt5_15 >= 0.275 and silt5_15 <= 0.5:
        layers['5_15cm'] = 'loam' 
    elif (clay5_15 <= 0.275 and clay5_15 >= 0.125 and silt5_15 >= 0.5) or (clay5_15 <= 0.125 and silt5_15 >= 0.5 and silt5_15 <= 0.8):
        layers['5_15cm'] = 'silt loam' 
    elif clay5_15 <= 0.125 and silt5_15 >= 0.8:
        layers['5_15cm'] = 'silt'
    elif sand5_15 >= 0.9:
        layers['5_15cm'] = 'sand'
    elif sand5_15 >= 0.8:
        layers['5_15cm'] = 'loamy sand'
    else:
        layers['5_15cm'] = 'sandy loam'

    # 15-30 cm
    if clay15_30 >= 0.4 and sand15_30 <= 0.45 and silt15_30 <= 0.4:
        layers['15_30cm'] = 'clay'
    elif clay15_30 >= 0.4 and silt15_30 >= 0.4:
        layers['15_30cm'] = 'silty clay'
    elif clay15_30 >= 0.35 and sand15_30 >= 0.45:
        layers['15_30cm'] = 'sandy clay'
    elif clay15_30 >= 0.2 and clay15_30 <= 0.35 and sand15_30 >= 0.45 and silt15_30 <= 0.275:
        layers['15_30cm'] = 'sandy clay loam'
    elif clay15_30 >= 0.275 and clay15_30 <= 0.4 and sand15_30 >= 0.2 and sand15_30 <= 0.45:
        layers['15_30cm'] = 'clay loam'
    elif clay15_30 >= 0.275 and clay15_30 <= 0.4 and sand15_30 <= 0.2:
        layers['15_30cm'] = 'silty clay loam'
    elif clay15_30 >= 0.075 and clay15_30 <= 0.275 and sand15_30 <= 0.525 and silt15_30 >= 0.275 and silt15_30 <= 0.5:
        layers['15_30cm'] = 'loam' 
    elif (clay15_30 <= 0.275 and clay15_30 >= 0.125 and silt15_30 >= 0.5) or (clay15_30 <= 0.125 and silt15_30 >= 0.5 and silt15_30 <= 0.8):
        layers['15_30cm'] = 'silt loam' 
    elif clay15_30 <= 0.125 and silt15_30 >= 0.8:
        layers['15_30cm'] = 'silt'
    elif sand15_30 >= 0.9:
        layers['15_30cm'] = 'sand'
    elif sand15_30 >= 0.8:
        layers['15_30cm'] = 'loamy sand'
    else:
        layers['15_30cm'] = 'sandy loam'

    return layers


def soiltype2optimalmoisture(dict):
    soiltype0_5 = dict['0_5cm']
    soiltype5_15 = dict['5_15cm']
    soiltype15_30 = dict['15_30cm']

    optmoisture = {}

    # https://cropintel.ca/agronomy-insights?i=15
    match soiltype0_5:
        case 'clay':                optmoisture['0_5cm'] = [0.19, 0.41]
        case 'silty clay':          optmoisture['0_5cm'] = [0.165, 0.38]
        case 'sandy clay':          optmoisture['0_5cm'] = [0.165, 0.365]
        case 'sandy clay loam':     optmoisture['0_5cm'] = [0.14, 0.325]
        case 'clay loam':           optmoisture['0_5cm'] = [0.165, 0.375]
        case 'silty clay loam':     optmoisture['0_5cm'] = [0.16, 0.375]
        case 'loam':                optmoisture['0_5cm'] = [0.105, 0.385]
        case 'silt loam':           optmoisture['0_5cm'] = [0.105, 0.37]
        case 'silt':                optmoisture['0_5cm'] = [0.14, 0.365]
        case 'sand':                optmoisture['0_5cm'] = [0.055, 0.12]
        case 'loamy sand':          optmoisture['0_5cm'] = [0.075, 0.235]
        case 'sandy loam':          optmoisture['0_5cm'] = [0.09, 0.24]
        case _:                     optmoisture['0_5cm'] = [1, 1]
    
    match soiltype5_15:
        case 'clay':                optmoisture['5_15cm'] = [0.19, 0.41]
        case 'silty clay':          optmoisture['5_15cm'] = [0.165, 0.38]
        case 'sandy clay':          optmoisture['5_15cm'] = [0.165, 0.365]
        case 'sandy clay loam':     optmoisture['5_15cm'] = [0.14, 0.325]
        case 'clay loam':           optmoisture['5_15cm'] = [0.165, 0.375]
        case 'silty clay loam':     optmoisture['5_15cm'] = [0.16, 0.375]
        case 'loam':                optmoisture['5_15cm'] = [0.105, 0.385]
        case 'silt loam':           optmoisture['5_15cm'] = [0.105, 0.37]
        case 'silt':                optmoisture['5_15cm'] = [0.14, 0.365]
        case 'sand':                optmoisture['5_15cm'] = [0.055, 0.12]
        case 'loamy sand':          optmoisture['5_15cm'] = [0.075, 0.235]
        case 'sandy loam':          optmoisture['5_15cm'] = [0.09, 0.24]
        case _:                     optmoisture['5_15cm'] = [1, 1]

    match soiltype15_30:
        case 'clay':                optmoisture['15_30cm'] = [0.19, 0.41]
        case 'silty clay':          optmoisture['15_30cm'] = [0.165, 0.38]
        case 'sandy clay':          optmoisture['15_30cm'] = [0.165, 0.365]
        case 'sandy clay loam':     optmoisture['15_30cm'] = [0.14, 0.325]
        case 'clay loam':           optmoisture['15_30cm'] = [0.165, 0.375]
        case 'silty clay loam':     optmoisture['15_30cm'] = [0.16, 0.375]
        case 'loam':                optmoisture['15_30cm'] = [0.105, 0.385]
        case 'silt loam':           optmoisture['15_30cm'] = [0.105, 0.37]
        case 'silt':                optmoisture['15_30cm'] = [0.14, 0.365]
        case 'sand':                optmoisture['15_30cm'] = [0.055, 0.12]
        case 'loamy sand':          optmoisture['15_30cm'] = [0.075, 0.235]
        case 'sandy loam':          optmoisture['15_30cm'] = [0.09, 0.24]
        case _:                     optmoisture['15_30cm'] = [1, 1]

    return optmoisture

# print(latlon2rawsoildata(LATITUDE, LONGITUDE))

# print("-" * 20)

# print(rawsoildata2soiltype(latlon2rawsoildata(LATITUDE, LONGITUDE)))

# print("-" * 20)

# print(soiltype2optimalmoisture(rawsoildata2soiltype(latlon2rawsoildata(LATITUDE, LONGITUDE))))