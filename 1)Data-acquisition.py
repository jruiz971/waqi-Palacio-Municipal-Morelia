"""
The license we use in this project is the "GNU General Public License v3.0"

Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
"""

import json
import requests
from datetime import datetime
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

#--- Download data from server ---#
response = requests.get("https://api.waqi.info/feed/morelia/?token=YOUR-TOKEN-HERE") 
"""
API Token Request Form https://aqicn.org/data-platform/token/#/
"""

Raw_data = response.json()
print (Raw_data)
keys = Raw_data.keys() # ['status','data']
Raw_data.pop('status') #Clean data

#---Gathering information ---#
latitude,longitude,name = 19.702153, -101.190948,'Palacio Municipal, Morelia, Mexico'
aqi = Raw_data['data'].get('aqi') #Real-time air quality infomrmation.

iaqi = Raw_data['data'].get('iaqi')
#print(iaqi.keys())
#dict_keys(['dew', 'h', 'o3', 'p', 'pm25', 't', 'w'])
o3 = iaqi.get('o3')
o3_value = o3.get('v')
pm25 = iaqi.get('pm25')
pm25_value = pm25.get('v')

time = Raw_data['data'].get('time')
datestring = time.get('s') #String
dt = datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')

year = dt.year
month = dt.month
day = dt.day

hour = dt.hour
minute = dt.minute
second = dt.second


#---Data for the json file ---#
save_file = {
    'latitude' : latitude,
    'longitude': longitude,
    'name' : name,

    'o3' : o3_value,
    'pm25' : pm25_value,

    'year' : dt.year,
    'month' : dt.month,
    'day' : dt.day,

    'hour' : dt.hour,
    'minute' : dt.minute,
    'second' : dt.second
}

today = datetime.today().strftime('%Y-%m-%d:%H-%M-%S')

#--- Create the json file ---#
file_name = "Pollutants_measurements.json"
with open(file_name,'w') as json_file:
    json.dump(save_file,json_file)
