# from flask import Flask, render_template, flash
from flask import Flask,render_template,request,redirect,url_for

import mysql.connector
from mysql.connector import errorcode
import json
import glob
import datetime
import subprocess
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('graphics.html',trending=trending,today=date.today().strftime("%d/%m/%Y"))
    # return('<h1>Hola</h1>')
    return render_template('home.html')

@app.route('/Measurements', methods=['POST'])
def usuario_up():

    Pollutant=request.form['Pollutants']
    Date=request.form['date']
    #print(Pollutant, Date)
    #2020-08-11
    year = (Date[0:4])
    month = (Date[5:7])
    day = (Date[8:])
    # # return ("<h1>Hola</h1>")
    # return redirect(url_for('trend'))


    PATHDBCONNECTION= '/home/luis/Documentos/UNAM/CuartoSemestre/ComputoDistribuido/dbconnection/'
    today = datetime.today()#.strftime('%Y-%m-%d')

    with open(PATHDBCONNECTION+'db.json') as json_file:
        config = json.load(json_file)

    o3Array = []; pm25Array = []; hourArray =[]
    PollutantQuery=[]; hourArray=[]
    try:
        cnx = mysql.connector.connect(**config,auth_plugin='mysql_native_password')
        cursor = cnx.cursor()

        # +-----------+-------------+------------------------------------+-------+-------+------+-------+------+------+--------+--------+
        # | latitude  | longitude   | name                               | o3    | pm25  | year | month | day  | hour | minute | second |
        # +-----------+-------------+------------------------------------+-------+-------+------+-------+------+------+--------+--------+
        # | 19.702153 | -101.190948 | Palacio Municipal, Morelia, Mexico | 34.40 | 34.00 | 2020 | 7     | 22   | 14   | 0      | 0      |
        # +-----------+-------------+------------------------------------+-------+-------+------+-------+------+------+--------+--------+

        #query = ("SELECT  DISTINCT o3,pm25,hour FROM Measurements WHERE year='%s' AND month='%s' AND day='%s'" %(today.year, today.month, today.day))
        # query = ("SELECT  DISTINCT o3, hour FROM Measurements WHERE year='%s' AND month='%s' AND day='%s'" %(year, month, day))
        # cursor.execute(query)
        # for o3,hour in cursor:
        #     PollutantQuery.append(Pollutant)
        #     hourArray.append(hour)

        print(year, month, day,Pollutant)
        query = """SELECT  DISTINCT %s,hour FROM Measurements WHERE year=%s AND month=%s AND day=%s""" %(Pollutant,year,month,day)
        #data_query=(Pollutant,year,month,day)
        cursor.execute(query)
        data=cursor.fetchall()
        
        for registro in data:
            #print(data)
            PollutantQuery.append(registro[0])
            hourArray.append(registro[1])
        print( PollutantQuery)
        print(hourArray)
            #o3Array.append(data[0])
            #pm25Array.append(pm25)
            #hourArray.append(hour)
        print("a")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
        cnx.close()

    #print(o3Array,pm25Array,hourArray)  

    #---- PLOT ----#
    x = np.arange(len(hourArray))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, PollutantQuery, width, label=Pollutant)
    #rects2 = ax.bar(x + width/2, pm25Array, width, label='pm2.5')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Niveles')
    ax.set_xlabel('Hora del día')
    date = datetime.today().strftime('%Y-%m-%d')
    ax.set_title('Mediciones del día: '+date+'\n Niveles de Ozono y Partículas Suspendidas menores a 2.5 micrometros. \n Estación: Palacio Municipal, Morelia, Mexico.')
    ax.set_xticks(x)
    ax.set_xticklabels(hourArray)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    #autolabel(rects2)

    fig.tight_layout()

    PATH ='/home/luis/Downloads/Pagina-Desarrollo/static/img/'
    plt.savefig(PATH+Pollutant+Date)


    plt.show()


    return render_template('request.html',id=Pollutant+Date)


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0') # TRUE -> Reinicia el server para ver los cambios. HOST 0000, es para acceder desde otro dispositivo en la red local
