"""
The license we use in this project is the "GNU General Public License v3.0"

Juan Luis Ruiz Vanegas -> juanluisruiz971@gmail.com

Currently working remotely, a json file with credentials per database is needed.
"""
#Further libraries might be needed

import mysql
import mysql.connector
from mysql.connector import errorcode
import json
import glob
import subprocess

#---Insertion query function with connector and cursor. ---#
def insertar (data_query):
    try:
        cnx=mysql.connector.connect(**config,auth_plugin='mysql_native_password')
        cursor=cnx.cursor()
        query=("INSERT INTO Measurements (latitude,longitude, name, o3, pm25, year, month, day, hour, minute, second) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
        print ("f")
        cursor.execute(query,data_query)
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
                
    else:
        cnx.close()



if __name__ == "__main__":
    # You need a json file with your db credentials. Here you have to puth the path
    PATHDBCONNECTION= '/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/dbconnection/'
    
    PATHJSONFILE='/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/Projects/waqi-Palacio-Municipal-Morelia/'
    #Here you have to put the path where your json file wit your data to be storaged is

    with open(PATHDBCONNECTION+'db.json') as json_file:
            config=json.load(json_file)
    
    for filename in glob.glob(PATHJSONFILE+"*.json"):
        print(filename)  ##Use this to show the path and the file-name.
        
        real_file =filename[101:] #In this vector you have to put where your file name begins, ie, 82

        with open(real_file,'r') as f:
            data=json.load(f)
        
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        name = data.get('name')
        o3 = data.get('o3')
        pm25 = data.get('pm25')
        year = data.get('year')
        month = data.get('month')
        day = data.get('day')
        hour = data.get('hour')
        minute = data.get('minute')
        second = data.get('second')

        data_query = (latitude,longitude, name, o3, pm25, year, month, day, hour, minute, second)
        insertar(data_query)

    #--- Move the json file to a backup directory ---#
    output = subprocess.run(["mv",filename,PATHJSONFILE+"Backup/"])