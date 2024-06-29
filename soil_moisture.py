# Code taking and interpreting soil data for a location
# Created:     2024-01-22
# Modified:    2024-06-18 (last status: working fine)
# Author:      Kagan Dikmen

import requests
# from geopy.geocoders import Nominatim
# import geopy.point

# TODO: think of a way of implementing the error message better

# LATITUDE = float(input("Latitude: "))
# LONGITUDE = float(input("Longitude: "))

# p = geopy.point.Point(LATITUDE, LONGITUDE)
# r = Nominatim(user_agent = "Florens").reverse(p)
# print("This lat-lon pair correspond to: " + str(r))

class Soil:

    def __init__(self, lat, lon):
        
        TEMPLATE_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
        response = requests.get(TEMPLATE_URL).json()

        self.clay_data = response['properties']['layers'][0]['depths']
        self.sand_data = response['properties']['layers'][1]['depths']
        self.silt_data = response['properties']['layers'][2]['depths']

    def rawSoilData(self):
        try: 
            self.clay_p_0_5cm    = self.clay_data[0]['values']['Q0.5'] / 1000
            self.clay_p_5_15cm   = self.clay_data[1]['values']['Q0.5'] / 1000
            self.clay_p_15_30cm  = self.clay_data[2]['values']['Q0.5'] / 1000
        
            self.sand_p_0_5cm    = self.sand_data[0]['values']['Q0.5'] / 1000
            self.sand_p_5_15cm   = self.sand_data[1]['values']['Q0.5'] / 1000
            self.sand_p_15_30cm  = self.sand_data[2]['values']['Q0.5'] / 1000
        
            self.silt_p_0_5cm    = self.silt_data[0]['values']['Q0.5'] / 1000
            self.silt_p_5_15cm   = self.silt_data[1]['values']['Q0.5'] / 1000
            self.silt_p_15_30cm  = self.silt_data[2]['values']['Q0.5'] / 1000
        except:
            print("ERROR: There is no soil data for the given location. It may be in a residential area or a water body.")

    def soilType(self):

        layers = {}
        
        # 0-5 cm
        if self.clay_p_0_5cm >= 0.4 and self.sand_p_0_5cm <= 0.45 and self.silt_p_0_5cm <= 0.4:
            layers['0_5cm'] = 'clay'
        elif self.clay_p_0_5cm >= 0.4 and self.silt_p_0_5cm >= 0.4:
            layers['0_5cm'] = 'silty clay'
        elif self.clay_p_0_5cm >= 0.35 and self.sand_p_0_5cm >= 0.45:
            layers['0_5cm'] = 'sandy clay'
        elif self.clay_p_0_5cm >= 0.2 and self.clay_p_0_5cm <= 0.35 and self.sand_p_0_5cm >= 0.45 and self.silt_p_0_5cm <= 0.275:
            layers['0_5cm'] = 'sandy clay loam'
        elif self.clay_p_0_5cm >= 0.275 and self.clay_p_0_5cm <= 0.4 and self.sand_p_0_5cm >= 0.2 and self.sand_p_0_5cm <= 0.45:
            layers['0_5cm'] = 'clay loam'
        elif self.clay_p_0_5cm >= 0.275 and self.clay_p_0_5cm <= 0.4 and self.sand_p_0_5cm <= 0.2:
            layers['0_5cm'] = 'silty clay loam'
        elif self.clay_p_0_5cm >= 0.075 and self.clay_p_0_5cm <= 0.275 and self.sand_p_0_5cm <= 0.525 and self.silt_p_0_5cm >= 0.275 and self.silt_p_0_5cm <= 0.5:
            layers['0_5cm'] = 'loam' 
        elif (self.clay_p_0_5cm <= 0.275 and self.clay_p_0_5cm >= 0.125 and self.silt_p_0_5cm >= 0.5) or (self.clay_p_0_5cm <= 0.125 and self.silt_p_0_5cm >= 0.5 and self.silt_p_0_5cm <= 0.8):
            layers['0_5cm'] = 'silt loam' 
        elif self.clay_p_0_5cm <= 0.125 and self.silt_p_0_5cm >= 0.8:
            layers['0_5cm'] = 'silt'
        elif self.sand_p_0_5cm >= 0.9:
            layers['0_5cm'] = 'sand'
        elif self.sand_p_0_5cm >= 0.8:
            layers['0_5cm'] = 'loamy sand'
        else:
            layers['0_5cm'] = 'sandy loam'

        # 5-15 cm
        if self.clay_p_5_15cm >= 0.4 and self.sand_p_5_15cm <= 0.45 and self.silt_p_5_15cm <= 0.4:
            layers['5_15cm'] = 'clay'
        elif self.clay_p_5_15cm >= 0.4 and self.silt_p_5_15cm >= 0.4:
            layers['5_15cm'] = 'silty clay'
        elif self.clay_p_5_15cm >= 0.35 and self.sand_p_5_15cm >= 0.45:
            layers['5_15cm'] = 'sandy clay'
        elif self.clay_p_5_15cm >= 0.2 and self.clay_p_5_15cm <= 0.35 and self.sand_p_5_15cm >= 0.45 and self.silt_p_5_15cm <= 0.275:
            layers['5_15cm'] = 'sandy clay loam'
        elif self.clay_p_5_15cm >= 0.275 and self.clay_p_5_15cm <= 0.4 and self.sand_p_5_15cm >= 0.2 and self.sand_p_5_15cm <= 0.45:
            layers['5_15cm'] = 'clay loam'
        elif self.clay_p_5_15cm >= 0.275 and self.clay_p_5_15cm <= 0.4 and self.sand_p_5_15cm <= 0.2:
            layers['5_15cm'] = 'silty clay loam'
        elif self.clay_p_5_15cm >= 0.075 and self.clay_p_5_15cm <= 0.275 and self.sand_p_5_15cm <= 0.525 and self.silt_p_5_15cm >= 0.275 and self.silt_p_5_15cm <= 0.5:
            layers['5_15cm'] = 'loam' 
        elif (self.clay_p_5_15cm <= 0.275 and self.clay_p_5_15cm >= 0.125 and self.silt_p_5_15cm >= 0.5) or (self.clay_p_5_15cm <= 0.125 and self.silt_p_5_15cm >= 0.5 and self.silt_p_5_15cm <= 0.8):
            layers['5_15cm'] = 'silt loam' 
        elif self.clay_p_5_15cm <= 0.125 and self.silt_p_5_15cm >= 0.8:
            layers['5_15cm'] = 'silt'
        elif self.sand_p_5_15cm >= 0.9:
            layers['5_15cm'] = 'sand'
        elif self.sand_p_5_15cm >= 0.8:
            layers['5_15cm'] = 'loamy sand'
        else:
            layers['5_15cm'] = 'sandy loam'

        # 15-30 cm
        if self.clay_p_15_30cm >= 0.4 and self.sand_p_15_30cm <= 0.45 and self.silt_p_15_30cm <= 0.4:
            layers['15_30cm'] = 'clay'
        elif self.clay_p_15_30cm >= 0.4 and self.silt_p_15_30cm >= 0.4:
            layers['15_30cm'] = 'silty clay'
        elif self.clay_p_15_30cm >= 0.35 and self.sand_p_15_30cm >= 0.45:
            layers['15_30cm'] = 'sandy clay'
        elif self.clay_p_15_30cm >= 0.2 and self.clay_p_15_30cm <= 0.35 and self.sand_p_15_30cm >= 0.45 and self.silt_p_15_30cm <= 0.275:
            layers['15_30cm'] = 'sandy clay loam'
        elif self.clay_p_15_30cm >= 0.275 and self.clay_p_15_30cm <= 0.4 and self.sand_p_15_30cm >= 0.2 and self.sand_p_15_30cm <= 0.45:
            layers['15_30cm'] = 'clay loam'
        elif self.clay_p_15_30cm >= 0.275 and self.clay_p_15_30cm <= 0.4 and self.sand_p_15_30cm <= 0.2:
            layers['15_30cm'] = 'silty clay loam'
        elif self.clay_p_15_30cm >= 0.075 and self.clay_p_15_30cm <= 0.275 and self.sand_p_15_30cm <= 0.525 and self.silt_p_15_30cm >= 0.275 and self.silt_p_15_30cm <= 0.5:
            layers['15_30cm'] = 'loam' 
        elif (self.clay_p_15_30cm <= 0.275 and self.clay_p_15_30cm >= 0.125 and self.silt_p_15_30cm >= 0.5) or (self.clay_p_15_30cm <= 0.125 and self.silt_p_15_30cm >= 0.5 and self.silt_p_15_30cm <= 0.8):
            layers['15_30cm'] = 'silt loam' 
        elif self.clay_p_15_30cm <= 0.125 and self.silt_p_15_30cm >= 0.8:
            layers['15_30cm'] = 'silt'
        elif self.sand_p_15_30cm >= 0.9:
            layers['15_30cm'] = 'sand'
        elif self.sand_p_15_30cm >= 0.8:
            layers['15_30cm'] = 'loamy sand'
        else:
            layers['15_30cm'] = 'sandy loam'

        return layers
    
    def optimalMoisture(self, layersDict):

        soiltype0_5     = layersDict['0_5cm']
        soiltype5_15    = layersDict['5_15cm']
        soiltype15_30   = layersDict['15_30cm']

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