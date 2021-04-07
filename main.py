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
    c.execute("select * from study_locations ORDER BY totaal DESC;")
    column_names = [description[0] for description in c.description]
    # c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    conn.row_factory = dict_factory
    c.execute("select * from study_locations ORDER BY totaal DESC;")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations ORDER BY totaal DESC;")
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
    return render_template("test1.html")


@app.route('/<variable>', methods=['GET'])
def location_page(variable):
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect('test.db')
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("select * from study_locations ORDER BY totaal DESC;")
    column_names = [description[0] for description in c.description]
    # c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    conn.row_factory = dict_factory
    c.execute("select * from study_locations ORDER BY totaal DESC;")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations ORDER BY totaal DESC;")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[0] for study_locations_tuple in study_locations_tuples]

    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()
    if variable in study_locations_list:
        c.execute("SELECT * FROM study_locations WHERE werkplek = '{idf}'".format(idf=variable))
        data1 = c.fetchall()
        # data1 = c.execute("SELECT werkplek FROM study_locations WHERE werkplek = 'TU Delft Bibliotheek'")
    return render_template("modal.html", study_locations=variable, data=data1, column_names=column_names)


if __name__ == "__main__":
    app.run(debug=True)