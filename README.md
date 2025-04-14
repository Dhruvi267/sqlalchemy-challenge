# 🌴 SQLAlchemy Climate Analysis & Flask API Project

This project explores historical climate data in Honolulu, Hawaii using SQLAlchemy, SQLite, Pandas, and Matplotlib — then serves that data through a dynamic Flask API. It’s a complete end-to-end demonstration of backend logic and data storytelling using real-world weather data.

---

## 📈 Project Goals

- Analyze historical weather patterns in Hawaii using ORM queries
- Visualize precipitation and temperature trends over the last year of data
- Build a Flask API to serve insights dynamically with both static and parameterized routes

---

## 🗂️ Project Structure

```
sqlalchemy-challenge/
│
├── SurfsUp/
│   ├── climate_starter.ipynb   # Climate data analysis with SQLAlchemy + Pandas
│   ├── app.py                  # Flask API routes to access the analysis results
│   └── Resources/
│       └── hawaii.sqlite       # SQLite database of weather data
```

---

## 📊 Climate Data Analysis

In `climate_starter.ipynb`, I used SQLAlchemy ORM to connect to the SQLite database and reflect the schema automatically.

### ✅ Steps Covered

- Connected to the SQLite database with SQLAlchemy `create_engine()`
- Reflected existing tables into ORM classes using `automap_base()`
- Linked to the database with a session

### 📌 Precipitation Analysis
- Retrieved the most recent date in the dataset
- Queried precipitation data for the previous 12 months
- Loaded the result into a Pandas DataFrame
- Sorted the DataFrame by date and plotted precipitation levels
- Displayed summary statistics for the precipitation

### 📌 Station Analysis
- Queried the total number of weather stations
- Identified the most active station (i.e., most records)
- Calculated the min, max, and average temperature for that station
- Retrieved TOBS (temperature observations) for the last year
- Visualized TOBS as a histogram

All sessions were properly closed after querying.

---

## 🌐 Flask API Routes

The second part of the project was to expose the data using a RESTful Flask API. The API is created in `app.py` and includes both static and dynamic routes.

| Route | Description |
|-------|-------------|
| `/` | Homepage with a list of available routes |
| `/api/v1.0/precipitation` | Returns precipitation data for the last 12 months as JSON |
| `/api/v1.0/stations` | Returns a list of all station IDs |
| `/api/v1.0/tobs` | Returns temperature observations for the most active station over the last 12 months |
| `/api/v1.0/<start>` | Returns min, avg, and max temperatures from a given start date to the end |
| `/api/v1.0/<start>/<end>` | Returns min, avg, and max temperatures for a given date range |

All routes return JSON and leverage SQLAlchemy ORM queries behind the scenes.

---

## 🧠 Skills Practiced

- Writing efficient ORM queries with SQLAlchemy
- Visualizing time series data with Pandas and Matplotlib
- Structuring and building APIs with Flask
- Dynamic route handling with query parameters
- Clean project management using Git and GitHub

---

