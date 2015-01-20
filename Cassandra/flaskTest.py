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

@app.route('/')
def index():
    script="./static/leaflet-0.7.3/leaflet.js"
    css="./static/leaflet-0.7.3/leaflet.css"
    title = "Japan Tsunami Map"
    datinf=datetime(2014, 12, 24, 10, 32)
    datsup=datetime(2015, 1, 5, 10, 32)
    lat_tsunami = 34.241238
    lon_tsunami = 137.433197
    datas = ca.alertPhones(datinf,datsup,lat_tsunami,lon_tsunami,500)
    return render_template('flask1.html',title=title,script=script,css=css,datas=datas,latTsunami=lat_tsunami,lonTsunami=lon_tsunami)

app.run()


