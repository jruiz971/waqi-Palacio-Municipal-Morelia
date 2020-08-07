# waqi-Palacio-Municipal-Morelia
 Air Pollution: Real-time Air Quality Index (AQI)
 
In this project I download information about Morelia air quality. I do request every 2 hours with crontab and save the information on a
 SQL server. The real time data images can be consulted on: http://132.247.186.67/skadoosh/waqi-Measurements-Palacio-Municipal-Morelia/Images/Morelia,Air-Quality.png  ; and the json file:  http://132.247.186.67/skadoosh/waqi-Measurements-Palacio-Municipal-Morelia/json-files/ ;



--REQUERIMENTS

WAQI Token:
 -API Token Request Form https://aqicn.org/data-platform/token/#/

python3 libraries:
	-json
	-request
	-matplotlib
	-numpy
	-mysql
	-mysql.connector
	-subprocess
	-glob

SQl Server
 -You can dowload following this instructions:
	

--TO RUN THE PROJECT
clone the repository.

Run 1)Data-acquisition.py in order to get the data about the air quality. This program will create a json file.

Then, run 2)StoreDB.py, this program will open the json file that you just created and will create a connection to a SQL Server. After 
that will insert the data on the json file in the SQL Server and close the connection to the SQL Server .

Last but not least, run 3)Data-Processing.py. Again, will open a connection to the SQL Server and will do some queries in order to crea
te a image of the air pollution.



CONTACT:
	-Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
