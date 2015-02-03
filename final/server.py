# -*- coding: utf-8 -*-

"""
------------------------------------------------
--- Japan Tsunami Project
--- Flask interface for web visualization
------------------------------------------------
"""

import os
import cities
from datetime import datetime
from flask import Flask, render_template, request,jsonify

tmpl_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=tmpl_dir)

japan_cities = getattr(cities,"cities")

"""datinf = datetime(2015, 1, 5, 10, 32)
datsup = datetime(2015, 1, 25, 10, 32)
lat_tsunami = 34.241238
lon_tsunami = 137.433197
rad = 500
datas = ca.alertPhones(datinf,datsup,lat_tsunami,lon_tsunami,rad)
"""

@app.route('/')
def index():
    #script="./static/leaflet-0.7.3/leaflet.js"
    #css="./static/leaflet-0.7.3/leaflet.css"
    title = "Japan Tsunami Map"
    return render_template('index.html',title=title,japancities=japan_cities)

@app.route('/tsunami',methods=["POST"])
def tsunami():
    lon = request.form["lon"]
    lat = request.form["lat"]
    dat = request.form["date"]


    return jsonify(status="node_down",node="todo")

app.run()
