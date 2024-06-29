# Code taking and interpreting current soil data for a location
# Created:     2024-06-29
# Modified:    2024-06-29 (last status: working fine)
# Author:      Kagan Dikmen

import requests

class SoilCurrent:

    cC = {}

    def __init__(self, lat, lon):
        
        BASE_URL = "https://api.open-meteo.com/v1/forecast?"
        URL_TEMPLATE = BASE_URL + "latitude=" + "%.2f" % lat + "&longitude=" + "%.2f" % lon

        #URL_ST0     = URL_TEMPLATE + "&hourly=soil_temperature_0cm"
        URL_ST6     = URL_TEMPLATE + "&hourly=soil_temperature_6cm"
        #URL_ST18    = URL_TEMPLATE + "&hourly=soil_temperature_18cm"
        #URL_ST54    = URL_TEMPLATE + "&hourly=soil_temperature_54cm"

        #URL_SM0_1   = URL_TEMPLATE + "&hourly=soil_moisture_0_to_1cm"
        #URL_SM1_3   = URL_TEMPLATE + "&hourly=soil_moisture_1_to_3cm"
        URL_SM3_9   = URL_TEMPLATE + "&hourly=soil_moisture_3_to_9cm"
        #URL_SM9_27  = URL_TEMPLATE + "&hourly=soil_moisture_9_to_27cm"
        #URL_SM27_81 = URL_TEMPLATE + "&hourly=soil_moisture_27_to_81cm"

        #response_st0        = requests.get(URL_ST0).json()
        response_st6        = requests.get(URL_ST6).json()
        #response_st18       = requests.get(URL_ST18).json()
        #response_st54       = requests.get(URL_ST54).json()

        #response_sm0_1      = requests.get(URL_SM0_1).json()
        #response_sm1_3      = requests.get(URL_SM1_3).json()
        response_sm3_9      = requests.get(URL_SM3_9).json()
        #response_sm9_27     = requests.get(URL_SM9_27).json()
        #response_sm27_81    = requests.get(URL_SM27_81).json()

        #self.st0_timelist    = response_st0['hourly']['time']
        #self.st0_vallist     = response_st0['hourly']['soil_temperature_0cm']
        self.st6_timelist    = response_st6['hourly']['time']
        self.st6_vallist     = response_st6['hourly']['soil_temperature_6cm']
        #self.st18_timelist   = response_st18['hourly']['time']
        #self.st18_vallist    = response_st18['hourly']['soil_temperature_18cm']
        #self.st54_timelist   = response_st54['hourly']['time']
        #self.st54_vallist    = response_st54['hourly']['soil_temperature_54cm']

        #self.sm0_1_timelist      = response_sm0_1['hourly']['time']
        #self.sm0_1_vallist       = response_sm0_1['hourly']['soil_moisture_0_to_1cm']
        #self.sm1_3_timelist      = response_sm1_3['hourly']['time']
        #self.sm1_3_vallist       = response_sm1_3['hourly']['soil_moisture_1_to_3cm']
        self.sm3_9_timelist      = response_sm3_9['hourly']['time']
        self.sm3_9_vallist       = response_sm3_9['hourly']['soil_moisture_3_to_9cm']
        #self.sm9_27_timelist     = response_sm9_27['hourly']['time']
        #self.sm9_27_vallist      = response_sm9_27['hourly']['soil_moisture_9_to_27cm']
        #self.sm27_81_timelist    = response_sm27_81['hourly']['time']
        #self.sm27_81_vallist     = response_sm27_81['hourly']['soil_moisture_27_to_81cm']

    def currentConditions(self):
        self.cC['tempData'] = self.st6_vallist
        self.cC['moistData'] = self.sm3_9_vallist
        return self.cC
