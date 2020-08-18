# waqi
#### CONTACT:
- Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com
- Andres Soto Millan -> hoblam500@gmail.com
#### Air Pollution: Real-time Air Quality Index (AQI)
![a4](https://user-images.githubusercontent.com/38228291/89695098-19e0f280-d913-11ea-86b8-ecfeacdae701.png)

In this project we download information about Morelia air quality, we do request every 2 hours with crontab and save the information on a SQL server.

#### OBJECTIVE

Our objective in this project is to collect Data that have the potential to become information to know the state of air quality in the city of Morelia using distributed computing tools and knowledge.

#### LICENSE 

We use the license **"GNU General Public License v3.0"** in this project.

[Link to license](https://github.com/jruiz971/waqi-Palacio-Municipal-Morelia/blob/master/LICENSE)

#### REQUERIMENTS

WAQI Token:
- API Token Request Form https://aqicn.org/data-platform/token/#/

python3 libraries:
> - json
>> - To use this libraryw, rite "import json" in your code once python has been downloaded to your device
> - request
>> - To install this library, use this command "pip3 install requests" in your console and then import the library into your code
> - matplotlib
>> - To install this library, use this command "pip3 install matplotlib" in your console and then import the library into your code.
> - numpy
>> - To install this library, use this command "pip3 install numpy" in your console and then import the library into your code.
> - mysql
>> - To install this library, use this command "pip3 install MySQL-python" in your console and then import the library into your code.
> - mysql.connector
>> - To install this library, use this command "pip install mysql-connector-python" in your console and then import the library into your code.
> - subprocess
>> - to use this module it is only necessary to import it
> - glob
>> - To install this library, use this command "Sudo pip3 install glob3" in your console and then import the library into your code.

#### DATABASE ADN SQl SERVER

- [Commands used in our database](https://github.com/jruiz971/waqi-Palacio-Municipal-Morelia/blob/master/MySQL-Comands.txt)

- [to learn how to connect to a database and MYSQL you can click here](https://www.neoguias.com/como-conectarse-a-mysql-usando-python/)


These are some screenshots of how we do it on our device and some commands that we use such as "USE" to select our database and the "DESCRIBE" command to see the structure of the DB
![Imagen de uso 1](https://user-images.githubusercontent.com/38228291/90460799-f84aec80-e104-11ea-97ec-997af9dbbdc3.jpeg)
![Imagen de uso 2](https://user-images.githubusercontent.com/38228291/90460881-2fb99900-e105-11ea-8a06-fbfa899be900.jpeg)

- Something important to mention is that when we open the credentials file for the SQL serer, the bd.json file must have the following information(This will be your file bd.json where you have to put your MySQL Server user and password):
> - {"user": "YOUR-USER-HERE", "password": "YOUR-PASSWORD-HERE", "host": "127.0.0.1", "database": "Measurement_Palacio_Municipal_Morelia", "raise_on_warnings": true}

#### TO RUN THE PROJECT
- Clone the repository---> https://github.com/jruiz971/waqi-Palacio-Municipal-Morelia.git
- The recommended way to work with this project is to execute the runs starting with run 1:

- Run 1) *Data-acquisition.py* in order to get the data about the air quality, this program will create a json file.

- Then, run 2) *StoreDB.py*, this program will open the json file that you just created and will create a connection to a SQL Server, after 
that will insert the data on the json file in the SQL Server and close the connection to the SQL Server .

- Last but not least, run 3)Data-Processing.py. Again, will open a connection to the SQL Server and will do some queries in order to crea
te a image of the air pollution.

- To enter our remote web service and be able to see the data and work with them in a better way, use this command "python3 skadoosh.py" in the folder where it is located

#### RESULTS

- This graph is an example of the data we work with
![Morelia,Air-Quality](https://user-images.githubusercontent.com/38228291/90459748-7659c400-e102-11ea-9de7-885402666733.png)
- The real time data images can be consulted on: http://132.247.186.67/skadoosh/waqi-Measurements-Palacio-Municipal-Morelia/Images/Morelia,Air-Quality.png
- And the json file:  http://132.247.186.67/skadoosh/waqi-Measurements-Palacio-Municipal-Morelia/json-files/ ;


#### Bibliography
- [Data and Image](https://aqicn.org/data-platform/token/#/)


