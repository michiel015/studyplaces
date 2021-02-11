# -*- coding: utf-8 -*- 
# __author__: Adarsh Kalikadien #
import sqlite3
from flask import Flask, render_template, url_for
from utilities import *
app = Flask(__name__)


@app.route("/")
def home():
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect('test.db')
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("select * from study_locations")
    column_names = [description[0] for description in c.description]
    # c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    conn.row_factory = dict_factory
    c.execute("select * from study_locations")
    data = c.fetchall()
    c.execute("SELECT study_location FROM study_locations")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[0] for study_locations_tuple in study_locations_tuples]

    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()

    return render_template("home.html", study_locations=study_locations_list, data=data, column_names=column_names)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/test1")
def test1():
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect('test.db')
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    data = c.fetchall()
    column_names = [description[0] for description in c.description]
    return render_template("test1.html", data=data, column_names=column_names)


if __name__ == "__main__":
    app.run(debug=True)