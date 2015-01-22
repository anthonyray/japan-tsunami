# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 20:32:04 2015

@author: Paco
"""

"""
------------------------------------------------
--- Japan Tsunami Project
--- Flask interface for web visualization
------------------------------------------------
"""

import os
import cassandraTest as ca
from datetime import datetime
from flask import Flask, render_template

tmpl_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=tmpl_dir)

japan_cities = list()
japan_cities.append(("Tokyo","9 128 090","http://en.wikipedia.org/wiki/Tokyo",35.732727,139.722404))
japan_cities.append(("Yokohama","3 709 777","http://en.wikipedia.org/wiki/Yokohama",35.462635,139.774854))
japan_cities.append(("Osaka","2 685 218","http://en.wikipedia.org/wiki/Osaka",34.705359,135.500729))
japan_cities.append(("Nagoya","2 275 428","http://en.wikipedia.org/wiki/Nagoya",35.193866,136.907394))
japan_cities.append(("Sapporo","1 919 684","http://en.wikipedia.org/wiki/Sapporo",43.179025,141.388028))
japan_cities.append(("Kobe","1 538 281","http://en.wikipedia.org/wiki/Kobe",34.699714,135.187619))
japan_cities.append(("Fukuoka","1 516 575","http://en.wikipedia.org/wiki/Fukuoka",33.643127,130.355035))
japan_cities.append(("Kyoto","1 469 912","http://en.wikipedia.org/wiki/Kyoto",35.043493,135.771593))
japan_cities.append(("Kawasaki","1 459 191","http://en.wikipedia.org/wiki/Kawasaki",35.557485,139.698357))
japan_cities.append(("Saitama","1 250 407","http://en.wikipedia.org/wiki/Saitama",35.867481,139.642576))

datinf=datetime(2015, 1, 5, 10, 32)
datsup=datetime(2015, 1, 25, 10, 32)
lat_tsunami = 34.241238
lon_tsunami = 137.433197
rad = 500

datas = ca.alertPhones(datinf,datsup,lat_tsunami,lon_tsunami,rad)


@app.route('/')
def index():
    script="./static/leaflet-0.7.3/leaflet.js"
    css="./static/leaflet-0.7.3/leaflet.css"
    title = "Japan Tsunami Map"
    return render_template('flask1.html',title=title,script=script,css=css,datas=datas,latTsunami=lat_tsunami,lonTsunami=lon_tsunami,japancities=japan_cities)

app.run()


