# waqi-Palacio-Municipal-Morelia
#### Air Pollution: Real-time Air Quality Index (AQI)
![4](https://user-images.githubusercontent.com/38228291/89688935-87852280-d903-11ea-8447-0a15de2b84f1.jpg)

In this project we download information about Morelia air quality, we do request every 2 hours with crontab and save the information on a SQL server.
- The real time data images can be consulted on: http://132.247.186.67/skadoosh/waqi-Measurements-Palacio-Municipal-Morelia/Images/Morelia,Air-Quality.png
- And the json file:  http://132.247.186.67/skadoosh/waqi-Measurements-Palacio-Municipal-Morelia/json-files/ ;


#### REQUERIMENTS

WAQI Token:
- API Token Request Form https://aqicn.org/data-platform/token/#/

python3 libraries:
>> - json
>> - request
>> - matplotlib
>> - numpy
>> - mysql
>> - mysql.connector
>> - subprocess
>> - glob

SQl Server
- You can dowload following this instructions:
	

#### TO RUN THE PROJECT
- clone the repository---> https://github.com/jruiz971/waqi-Palacio-Municipal-Morelia.git

- Run 1) *Data-acquisition.py* in order to get the data about the air quality, this program will create a json file.

- Then, run 2) *StoreDB.py*, this program will open the json file that you just created and will create a connection to a SQL Server, after 
that will insert the data on the json file in the SQL Server and close the connection to the SQL Server .

- Last but not least, run 3)Data-Processing.py. Again, will open a connection to the SQL Server and will do some queries in order to crea
te a image of the air pollution.

#### Bibliography
- [Image](https://www.esa.int/Enabling_Support/Preparing_for_the_Future/Space_for_Earth/Space_for_health/Air_quality_and_pollution)

#### CONTACT:
- Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
- Andres Soto Millan -> hoblam500@gmail.com
