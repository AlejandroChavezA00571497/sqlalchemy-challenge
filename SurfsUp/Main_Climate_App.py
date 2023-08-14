# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
import datetime as dt
import numpy as np



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station



# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)



#################################################
# Flask Routes
#################################################

#1.- Home Page
@app.route("/")
def home():
    print("Welcome to the Home Page")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


#2.- Precipitation Analysis into JSON:
@app.route("/api/v1.0/precipitation")
def precipitation():
    most_recent_date =  session.query(measurement.date).order_by(measurement.date.desc()).first()
    one_year_from_last_date = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    precipitation_scores = session.query(measurement.date, measurement.prcp).filter(measurement.date >= one_year_from_last_date).order_by(measurement.date).all()
    precipitation_list = []
    for date, prcp in precipitation_scores:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = prcp
        precipitation_list.append(precipitation_dict)



    return jsonify(precipitation_list)




#3.- Station Information into JSON:
@app.route("/api/v1.0/stations")
def stations():
    all_stations_data = session.quey(station.id, station.station, station.name, station.latitude, station.longitude, station.elevation).all()
    all_stations_list = []
    for id, station, name, latitude, longitude, elevation in all_stations_data:
        station_dict = {}
        station_dict["id"] = id
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations_list.append(station_dict)

    return jsonify(all_stations_list)




#4.- Temperature Observations (Most active station in a year) into JSON:
@app.route("/api/v1.0/tobs")
def tobs():
    one_year_from_last_date = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    stations_activity = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc())
    most_active_station = stations_activity.first()[0]
    tobs_data = session.query(measurement.date, measurement.tobs).filter(measurement.station == most_active_station).filter(measurement.date >= one_year_from_last_date).all()
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)



#5.- TOBS Stats Start into JSON:
@app.route("/api/v1.0/<start>")
def stats_start():
    most_recent_date =  session.query(measurement.date).order_by(measurement.date.desc()).first()

   
    return jsonify()



