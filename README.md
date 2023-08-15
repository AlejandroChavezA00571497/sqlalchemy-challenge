# sqlalchemy-challenge
Module 10 Challenge for the Tec de Monterrey Data Analysis Bootcamp, Introduction to SQLAlchemy

Python and Jupyter Notebook files that interact with an sqlite file in order to get information to perform climate analysis, and both create a report in a Jupyter Notebook file as well as create an App that returns jsonified responses through Flask.

Main_SurfsUp.ipynb is the first script, which takes the data from an sqlite file and reflects it into SQLAlchemy ORM. An exploratory precipitation analysis is made, calculating the inches of rain per date across all observations, then an exploratory stations analysis is made, returning the information from the stations that performed the observations, and extracting which one was the most active in terms of number of observations.

Main_Climate_App.py is the second file, which similar to the last one, takes information from the same sqlite file, and saves references to the tables in said files, in variables. Different from the other script, this one uses Flask to create an API whereby defining routes, a user can acquire jsonified responses with the data contained in the sqlite file. This data is:
-Precipitation Information
-Station information
-Temperature Observations
-Statistical analysis of temperatures from a given date, to the end of observations
-Statistical analysis of temperatures from a given date, to and end date

The main files for this project are contained in the SurfsUp directory which also contains the Resources directory, that has the hawaii.sqlite file from which the Main scripts pull data from. Inside the Resources directory there are also CSVs for the tables inside of the sqlite file.


Contributions:
- Data Analysis Bootcamp Classes
- https://flask.palletsprojects.com/en/2.3.x/quickstart/
- https://docs.sqlalchemy.org/en/20/

