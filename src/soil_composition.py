# Code taking and interpreting soil composition data for a location
# Created:     2024-01-22
# Modified:    2024-06-30 (last status: working fine)
# Author:      Kagan Dikmen

import requests
# from geopy.geocoders import Nominatim
# import geopy.point

# LATITUDE = float(input("Latitude: "))
# LONGITUDE = float(input("Longitude: "))

# p = geopy.point.Point(LATITUDE, LONGITUDE)
# r = Nominatim(user_agent = "Florens").reverse(p)
# print("This lat-lon pair correspond to: " + str(r))

class SoilComposition:
    layers = {}
    optMoisture = {}
    
    def __init__(self, lat, lon):
        
        try:
            TEMPLATE_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
            response = requests.get(TEMPLATE_URL).json()

            self.clay_data = response['properties']['layers'][0]['depths']
            self.sand_data = response['properties']['layers'][1]['depths']
            self.silt_data = response['properties']['layers'][2]['depths']
            
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
            try:
                latN = lat + 0.05
                latS = lat - 0.05

                lonE = lon + 0.05
                lonW = lon - 0.05

                TEMPURL_N = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % latN) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                TEMPURL_S = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % latS) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                TEMPURL_E = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lonE) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                TEMPURL_W = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lonW) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                
                try:
                    response_N = requests.get(TEMPURL_N).json()
                    clay_data_N = response_N['properties']['layers'][0]['depths']
                    sand_data_N = response_N['properties']['layers'][1]['depths']
                    silt_data_N = response_N['properties']['layers'][2]['depths']
                except:
                    clay_data_N = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_N = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_N = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                try:
                    response_S = requests.get(TEMPURL_N).json()
                    clay_data_S = response_S['properties']['layers'][0]['depths']
                    sand_data_S = response_S['properties']['layers'][1]['depths']
                    silt_data_S = response_S['properties']['layers'][2]['depths']
                except:
                    clay_data_S = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_S = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_S = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                
                try:
                    response_E = requests.get(TEMPURL_N).json()
                    clay_data_E = response_E['properties']['layers'][0]['depths']
                    sand_data_E = response_E['properties']['layers'][1]['depths']
                    silt_data_E = response_E['properties']['layers'][2]['depths']
                except:
                    clay_data_E = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_E = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_E = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                
                try:
                    response_W = requests.get(TEMPURL_N).json()
                    clay_data_W = response_W['properties']['layers'][0]['depths']
                    sand_data_W = response_W['properties']['layers'][1]['depths']
                    silt_data_W = response_W['properties']['layers'][2]['depths']
                except:
                    clay_data_W = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_W = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_W = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]

                self.clay_p_0_5cm    = (clay_data_N[0]['values']['Q0.5'] + clay_data_S[0]['values']['Q0.5'] + clay_data_E[0]['values']['Q0.5'] + clay_data_W[0]['values']['Q0.5']) / 4000
                self.clay_p_5_15cm   = (clay_data_N[1]['values']['Q0.5'] + clay_data_S[1]['values']['Q0.5'] + clay_data_E[1]['values']['Q0.5'] + clay_data_W[1]['values']['Q0.5']) / 4000
                self.clay_p_15_30cm  = (clay_data_N[2]['values']['Q0.5'] + clay_data_S[2]['values']['Q0.5'] + clay_data_E[2]['values']['Q0.5'] + clay_data_W[2]['values']['Q0.5']) / 4000
            
                self.sand_p_0_5cm    = (sand_data_N[0]['values']['Q0.5'] + sand_data_S[0]['values']['Q0.5'] + sand_data_E[0]['values']['Q0.5'] + sand_data_W[0]['values']['Q0.5']) / 4000
                self.sand_p_5_15cm   = (sand_data_N[1]['values']['Q0.5'] + sand_data_S[1]['values']['Q0.5'] + sand_data_E[1]['values']['Q0.5'] + sand_data_W[1]['values']['Q0.5']) / 4000
                self.sand_p_15_30cm  = (sand_data_N[2]['values']['Q0.5'] + sand_data_S[2]['values']['Q0.5'] + sand_data_E[2]['values']['Q0.5'] + sand_data_W[2]['values']['Q0.5']) / 4000
            
                self.silt_p_0_5cm    = (silt_data_N[0]['values']['Q0.5'] + silt_data_S[0]['values']['Q0.5'] + silt_data_E[0]['values']['Q0.5'] + silt_data_W[0]['values']['Q0.5']) / 4000
                self.silt_p_5_15cm   = (silt_data_N[1]['values']['Q0.5'] + silt_data_S[1]['values']['Q0.5'] + silt_data_E[1]['values']['Q0.5'] + silt_data_W[1]['values']['Q0.5']) / 4000
                self.silt_p_15_30cm  = (silt_data_N[2]['values']['Q0.5'] + silt_data_S[2]['values']['Q0.5'] + silt_data_E[2]['values']['Q0.5'] + silt_data_W[2]['values']['Q0.5']) / 4000

            except:
                latN = lat + 0.5
                latS = lat - 0.5

                lonE = lon + 0.5
                lonW = lon - 0.5

                TEMPURL_N = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % latN) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                TEMPURL_S = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lon) + "&lat=" + str("%.2f" % latS) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                TEMPURL_E = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lonE) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                TEMPURL_W = "https://rest.isric.org/soilgrids/v2.0/properties/query?lon=" + str("%.2f" % lonW) + "&lat=" + str("%.2f" % lat) + "&property=clay&property=sand&property=silt&depth=0-5cm&depth=5-15cm&depth=15-30cm&value=Q0.5"
                
                try:
                    response_N = requests.get(TEMPURL_N).json()
                    clay_data_N = response_N['properties']['layers'][0]['depths']
                    sand_data_N = response_N['properties']['layers'][1]['depths']
                    silt_data_N = response_N['properties']['layers'][2]['depths']
                except:
                    clay_data_N = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_N = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_N = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                try:
                    response_S = requests.get(TEMPURL_N).json()
                    clay_data_S = response_S['properties']['layers'][0]['depths']
                    sand_data_S = response_S['properties']['layers'][1]['depths']
                    silt_data_S = response_S['properties']['layers'][2]['depths']
                except:
                    clay_data_S = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_S = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_S = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                
                try:
                    response_E = requests.get(TEMPURL_N).json()
                    clay_data_E = response_E['properties']['layers'][0]['depths']
                    sand_data_E = response_E['properties']['layers'][1]['depths']
                    silt_data_E = response_E['properties']['layers'][2]['depths']
                except:
                    clay_data_E = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_E = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_E = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                
                try:
                    response_W = requests.get(TEMPURL_N).json()
                    clay_data_W = response_W['properties']['layers'][0]['depths']
                    sand_data_W = response_W['properties']['layers'][1]['depths']
                    silt_data_W = response_W['properties']['layers'][2]['depths']
                except:
                    clay_data_W = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}] 
                    sand_data_W = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
                    silt_data_W = [{'range': {'top_depth': 0, 'bottom_depth': 5, 'unit_depth': 'cm'}, 'label': '0-5cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 5, 'bottom_depth': 15, 'unit_depth': 'cm'}, 'label': '5-15cm', 'values': {'Q0.5': 0}}, {'range': {'top_depth': 15, 'bottom_depth': 30, 'unit_depth': 'cm'}, 'label': '15-30cm', 'values': {'Q0.5': 0}}]
            
                self.clay_p_0_5cm    = (clay_data_N[0]['values']['Q0.5'] + clay_data_S[0]['values']['Q0.5'] + clay_data_E[0]['values']['Q0.5'] + clay_data_W[0]['values']['Q0.5']) / 4000
                self.clay_p_5_15cm   = (clay_data_N[1]['values']['Q0.5'] + clay_data_S[1]['values']['Q0.5'] + clay_data_E[1]['values']['Q0.5'] + clay_data_W[1]['values']['Q0.5']) / 4000
                self.clay_p_15_30cm  = (clay_data_N[2]['values']['Q0.5'] + clay_data_S[2]['values']['Q0.5'] + clay_data_E[2]['values']['Q0.5'] + clay_data_W[2]['values']['Q0.5']) / 4000
            
                self.sand_p_0_5cm    = (sand_data_N[0]['values']['Q0.5'] + sand_data_S[0]['values']['Q0.5'] + sand_data_E[0]['values']['Q0.5'] + sand_data_W[0]['values']['Q0.5']) / 4000
                self.sand_p_5_15cm   = (sand_data_N[1]['values']['Q0.5'] + sand_data_S[1]['values']['Q0.5'] + sand_data_E[1]['values']['Q0.5'] + sand_data_W[1]['values']['Q0.5']) / 4000
                self.sand_p_15_30cm  = (sand_data_N[2]['values']['Q0.5'] + sand_data_S[2]['values']['Q0.5'] + sand_data_E[2]['values']['Q0.5'] + sand_data_W[2]['values']['Q0.5']) / 4000
            
                self.silt_p_0_5cm    = (silt_data_N[0]['values']['Q0.5'] + silt_data_S[0]['values']['Q0.5'] + silt_data_E[0]['values']['Q0.5'] + silt_data_W[0]['values']['Q0.5']) / 4000
                self.silt_p_5_15cm   = (silt_data_N[1]['values']['Q0.5'] + silt_data_S[1]['values']['Q0.5'] + silt_data_E[1]['values']['Q0.5'] + silt_data_W[1]['values']['Q0.5']) / 4000
                self.silt_p_15_30cm  = (silt_data_N[2]['values']['Q0.5'] + silt_data_S[2]['values']['Q0.5'] + silt_data_E[2]['values']['Q0.5'] + silt_data_W[2]['values']['Q0.5']) / 4000

    def soilType(self):
        
        # 0-5 cm
        if self.clay_p_0_5cm >= 0.4 and self.sand_p_0_5cm <= 0.45 and self.silt_p_0_5cm <= 0.4:
            self.layers['0_5cm'] = 'clay'
        elif self.clay_p_0_5cm >= 0.4 and self.silt_p_0_5cm >= 0.4:
            self.layers['0_5cm'] = 'silty clay'
        elif self.clay_p_0_5cm >= 0.35 and self.sand_p_0_5cm >= 0.45:
            self.layers['0_5cm'] = 'sandy clay'
        elif self.clay_p_0_5cm >= 0.2 and self.clay_p_0_5cm <= 0.35 and self.sand_p_0_5cm >= 0.45 and self.silt_p_0_5cm <= 0.275:
            self.layers['0_5cm'] = 'sandy clay loam'
        elif self.clay_p_0_5cm >= 0.275 and self.clay_p_0_5cm <= 0.4 and self.sand_p_0_5cm >= 0.2 and self.sand_p_0_5cm <= 0.45:
            self.layers['0_5cm'] = 'clay loam'
        elif self.clay_p_0_5cm >= 0.275 and self.clay_p_0_5cm <= 0.4 and self.sand_p_0_5cm <= 0.2:
            self.layers['0_5cm'] = 'silty clay loam'
        elif self.clay_p_0_5cm >= 0.075 and self.clay_p_0_5cm <= 0.275 and self.sand_p_0_5cm <= 0.525 and self.silt_p_0_5cm >= 0.275 and self.silt_p_0_5cm <= 0.5:
            self.layers['0_5cm'] = 'loam' 
        elif (self.clay_p_0_5cm <= 0.275 and self.clay_p_0_5cm >= 0.125 and self.silt_p_0_5cm >= 0.5) or (self.clay_p_0_5cm <= 0.125 and self.silt_p_0_5cm >= 0.5 and self.silt_p_0_5cm <= 0.8):
            self.layers['0_5cm'] = 'silt loam' 
        elif self.clay_p_0_5cm <= 0.125 and self.silt_p_0_5cm >= 0.8:
            self.layers['0_5cm'] = 'silt'
        elif self.sand_p_0_5cm >= 0.9:
            self.layers['0_5cm'] = 'sand'
        elif self.sand_p_0_5cm >= 0.8:
            self.layers['0_5cm'] = 'loamy sand'
        else:
            self.layers['0_5cm'] = 'sandy loam'

        # 5-15 cm
        if self.clay_p_5_15cm >= 0.4 and self.sand_p_5_15cm <= 0.45 and self.silt_p_5_15cm <= 0.4:
            self.layers['5_15cm'] = 'clay'
        elif self.clay_p_5_15cm >= 0.4 and self.silt_p_5_15cm >= 0.4:
            self.layers['5_15cm'] = 'silty clay'
        elif self.clay_p_5_15cm >= 0.35 and self.sand_p_5_15cm >= 0.45:
            self.layers['5_15cm'] = 'sandy clay'
        elif self.clay_p_5_15cm >= 0.2 and self.clay_p_5_15cm <= 0.35 and self.sand_p_5_15cm >= 0.45 and self.silt_p_5_15cm <= 0.275:
            self.layers['5_15cm'] = 'sandy clay loam'
        elif self.clay_p_5_15cm >= 0.275 and self.clay_p_5_15cm <= 0.4 and self.sand_p_5_15cm >= 0.2 and self.sand_p_5_15cm <= 0.45:
            self.layers['5_15cm'] = 'clay loam'
        elif self.clay_p_5_15cm >= 0.275 and self.clay_p_5_15cm <= 0.4 and self.sand_p_5_15cm <= 0.2:
            self.layers['5_15cm'] = 'silty clay loam'
        elif self.clay_p_5_15cm >= 0.075 and self.clay_p_5_15cm <= 0.275 and self.sand_p_5_15cm <= 0.525 and self.silt_p_5_15cm >= 0.275 and self.silt_p_5_15cm <= 0.5:
            self.layers['5_15cm'] = 'loam' 
        elif (self.clay_p_5_15cm <= 0.275 and self.clay_p_5_15cm >= 0.125 and self.silt_p_5_15cm >= 0.5) or (self.clay_p_5_15cm <= 0.125 and self.silt_p_5_15cm >= 0.5 and self.silt_p_5_15cm <= 0.8):
            self.layers['5_15cm'] = 'silt loam' 
        elif self.clay_p_5_15cm <= 0.125 and self.silt_p_5_15cm >= 0.8:
            self.layers['5_15cm'] = 'silt'
        elif self.sand_p_5_15cm >= 0.9:
            self.layers['5_15cm'] = 'sand'
        elif self.sand_p_5_15cm >= 0.8:
            self.layers['5_15cm'] = 'loamy sand'
        else:
            self.layers['5_15cm'] = 'sandy loam'

        # 15-30 cm
        if self.clay_p_15_30cm >= 0.4 and self.sand_p_15_30cm <= 0.45 and self.silt_p_15_30cm <= 0.4:
            self.layers['15_30cm'] = 'clay'
        elif self.clay_p_15_30cm >= 0.4 and self.silt_p_15_30cm >= 0.4:
            self.layers['15_30cm'] = 'silty clay'
        elif self.clay_p_15_30cm >= 0.35 and self.sand_p_15_30cm >= 0.45:
            self.layers['15_30cm'] = 'sandy clay'
        elif self.clay_p_15_30cm >= 0.2 and self.clay_p_15_30cm <= 0.35 and self.sand_p_15_30cm >= 0.45 and self.silt_p_15_30cm <= 0.275:
            self.layers['15_30cm'] = 'sandy clay loam'
        elif self.clay_p_15_30cm >= 0.275 and self.clay_p_15_30cm <= 0.4 and self.sand_p_15_30cm >= 0.2 and self.sand_p_15_30cm <= 0.45:
            self.layers['15_30cm'] = 'clay loam'
        elif self.clay_p_15_30cm >= 0.275 and self.clay_p_15_30cm <= 0.4 and self.sand_p_15_30cm <= 0.2:
            self.layers['15_30cm'] = 'silty clay loam'
        elif self.clay_p_15_30cm >= 0.075 and self.clay_p_15_30cm <= 0.275 and self.sand_p_15_30cm <= 0.525 and self.silt_p_15_30cm >= 0.275 and self.silt_p_15_30cm <= 0.5:
            self.layers['15_30cm'] = 'loam' 
        elif (self.clay_p_15_30cm <= 0.275 and self.clay_p_15_30cm >= 0.125 and self.silt_p_15_30cm >= 0.5) or (self.clay_p_15_30cm <= 0.125 and self.silt_p_15_30cm >= 0.5 and self.silt_p_15_30cm <= 0.8):
            self.layers['15_30cm'] = 'silt loam' 
        elif self.clay_p_15_30cm <= 0.125 and self.silt_p_15_30cm >= 0.8:
            self.layers['15_30cm'] = 'silt'
        elif self.sand_p_15_30cm >= 0.9:
            self.layers['15_30cm'] = 'sand'
        elif self.sand_p_15_30cm >= 0.8:
            self.layers['15_30cm'] = 'loamy sand'
        else:
            self.layers['15_30cm'] = 'sandy loam'
    
    def optimalMoisture(self):

        soiltype0_5     = self.layers['0_5cm']
        soiltype5_15    = self.layers['5_15cm']
        soiltype15_30   = self.layers['15_30cm']  

        # https://cropintel.ca/agronomy-insights?i=15
        match soiltype0_5:
            case 'clay':                self.optMoisture['0_5cm'] = [0.19, 0.41]
            case 'silty clay':          self.optMoisture['0_5cm'] = [0.165, 0.38]
            case 'sandy clay':          self.optMoisture['0_5cm'] = [0.165, 0.365]
            case 'sandy clay loam':     self.optMoisture['0_5cm'] = [0.14, 0.325]
            case 'clay loam':           self.optMoisture['0_5cm'] = [0.165, 0.375]
            case 'silty clay loam':     self.optMoisture['0_5cm'] = [0.16, 0.375]
            case 'loam':                self.optMoisture['0_5cm'] = [0.105, 0.385]
            case 'silt loam':           self.optMoisture['0_5cm'] = [0.105, 0.37]
            case 'silt':                self.optMoisture['0_5cm'] = [0.14, 0.365]
            case 'sand':                self.optMoisture['0_5cm'] = [0.055, 0.12]
            case 'loamy sand':          self.optMoisture['0_5cm'] = [0.075, 0.235]
            case 'sandy loam':          self.optMoisture['0_5cm'] = [0.09, 0.24]
            case _:                     self.optMoisture['0_5cm'] = [1, 1]
        
        match soiltype5_15:
            case 'clay':                self.optMoisture['5_15cm'] = [0.19, 0.41]
            case 'silty clay':          self.optMoisture['5_15cm'] = [0.165, 0.38]
            case 'sandy clay':          self.optMoisture['5_15cm'] = [0.165, 0.365]
            case 'sandy clay loam':     self.optMoisture['5_15cm'] = [0.14, 0.325]
            case 'clay loam':           self.optMoisture['5_15cm'] = [0.165, 0.375]
            case 'silty clay loam':     self.optMoisture['5_15cm'] = [0.16, 0.375]
            case 'loam':                self.optMoisture['5_15cm'] = [0.105, 0.385]
            case 'silt loam':           self.optMoisture['5_15cm'] = [0.105, 0.37]
            case 'silt':                self.optMoisture['5_15cm'] = [0.14, 0.365]
            case 'sand':                self.optMoisture['5_15cm'] = [0.055, 0.12]
            case 'loamy sand':          self.optMoisture['5_15cm'] = [0.075, 0.235]
            case 'sandy loam':          self.optMoisture['5_15cm'] = [0.09, 0.24]
            case _:                     self.optMoisture['5_15cm'] = [1, 1]

        match soiltype15_30:
            case 'clay':                self.optMoisture['15_30cm'] = [0.19, 0.41]
            case 'silty clay':          self.optMoisture['15_30cm'] = [0.165, 0.38]
            case 'sandy clay':          self.optMoisture['15_30cm'] = [0.165, 0.365]
            case 'sandy clay loam':     self.optMoisture['15_30cm'] = [0.14, 0.325]
            case 'clay loam':           self.optMoisture['15_30cm'] = [0.165, 0.375]
            case 'silty clay loam':     self.optMoisture['15_30cm'] = [0.16, 0.375]
            case 'loam':                self.optMoisture['15_30cm'] = [0.105, 0.385]
            case 'silt loam':           self.optMoisture['15_30cm'] = [0.105, 0.37]
            case 'silt':                self.optMoisture['15_30cm'] = [0.14, 0.365]
            case 'sand':                self.optMoisture['15_30cm'] = [0.055, 0.12]
            case 'loamy sand':          self.optMoisture['15_30cm'] = [0.075, 0.235]
            case 'sandy loam':          self.optMoisture['15_30cm'] = [0.09, 0.24]
            case _:                     self.optMoisture['15_30cm'] = [1, 1]