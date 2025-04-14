# Import the dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker
import datetime as dt

#################################################
# Database Setup
#################################################

# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)  # Updated for deprecation warning

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session factory
SessionLocal = sessionmaker(bind=engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Available Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = SessionLocal()
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= one_year_ago).all()
    session.close()

    precip_dict = {date: prcp for date, prcp in results}
    return jsonify(precip_dict)


@app.route("/api/v1.0/stations")
def stations():
    session = SessionLocal()
    results = session.query(Station.station).all()
    session.close()

    stations_list = [station[0] for station in results]
    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    session = SessionLocal()
    most_active = session.query(Measurement.station)\
        .group_by(Measurement.station)\
        .order_by(func.count().desc()).first()[0]

    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == most_active)\
        .filter(Measurement.date >= one_year_ago).all()
    session.close()

    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in results]
    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start_date(start):
    session = SessionLocal()
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).all()
    session.close()

    temps = list(results[0])
    return jsonify({
        "Start Date": start,
        "Min Temp": temps[0],
        "Avg Temp": temps[1],
        "Max Temp": temps[2]
    })


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = SessionLocal()
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start)\
     .filter(Measurement.date <= end).all()
    session.close()

    temps = list(results[0])
    return jsonify({
        "Start Date": start,
        "End Date": end,
        "Min Temp": temps[0],
        "Avg Temp": temps[1],
        "Max Temp": temps[2]
    })


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
