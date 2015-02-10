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
import cassandraTest as cassandre
import time
import datetime


tmpl_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=tmpl_dir)

japan_cities = getattr(cities,"cities")

@app.route('/')
def index():
    #script="./static/leaflet-0.7.3/leaflet.js"
    #css="./static/leaflet-0.7.3/leaflet.css"
    title = "Japan Tsunami Map"
    return render_template('index.html',title=title,japancities=japan_cities)

@app.route('/tsunami',methods=["POST"])
def tsunami():
    # Parsing the request
    '''lon = float(request.form["lon"])
    lat = float(request.form["lat"])
    dat1 = datetime.datetime.strptime(request.form["date"],"%Y-%m-%dT%H:%M")
    dat2 = dat1 + datetime.timedelta(minutes=10)
    radius = 500
    size_req_t = 1000000

    keyspace = "jap1"
    table = "bigtable"
    '''
    #phones = cassandre.alertPhones(dat1,dat2,lat,lon,radius,size_req_t,table,keyspace)
    phones = [ [43.52,141.53,"DATE","888","Sap_65"],[35,140,"DATE","888","Sap_65"],[37.52,140.53,"DATE","888","Sap_65"]]
    return jsonify(status="node_down",phones=phones)

app.run()
