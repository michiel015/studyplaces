# __author__: Adarsh Kalikadien #
import sqlite3
from flask import Flask, render_template, url_for
import socket

from utilities import *
app = Flask(__name__)

hostname = socket.gethostname()

if hostname == 'werkplekwijzer':
    db_location = '/var/www/werkplekwijzer/werkplekwijzer/test.db'
else:
    db_location = 'test.db'


@app.route("/")
def home():
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect(db_location)
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("select * from study_locations ORDER BY totale_score DESC;")
    column_names = [description[0] for description in c.description]
    # format column names automatically
    for i, name in enumerate(column_names):
        new_name = name.split('_')
        new_name[0] = new_name[0].capitalize()
        column_names[i] = " ".join(new_name)
    # c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    conn.row_factory = dict_factory
    c.execute("select * from study_locations ORDER BY totale_score DESC;")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations ORDER BY totale_score DESC;")
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


@app.route("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml")


@app.route("/robot.txt")
def robot():
    return render_template("robot.txt")


@app.route("/plek_toevoegen")
def plek_toevoegen():
    return render_template("plek_toevoegen.html")


@app.route('/<variable>', methods=['GET'])
def location_page(variable):
    # establish database connection and make cursor
    try:
        conn = sqlite3.connect(db_location)
    except:
        print('could not establish connection to db')
        exit(1)
    c = conn.cursor()
    c.execute("select * from study_locations ORDER BY totale_score DESC;")
    column_names = [description[0] for description in c.description]
    # format column names automatically
    for i, name in enumerate(column_names):
        new_name = name.split('_')
        new_name[0] = new_name[0].capitalize()
        column_names[i] = " ".join(new_name)
    # c.execute("SELECT * FROM study_locations WHERE test_column_3 = 'test_data_3'")
    conn.row_factory = dict_factory
    c.execute("select * from study_locations ORDER BY totale_score DESC;")
    data = c.fetchall()
    c.execute("SELECT url_name FROM study_locations ORDER BY totale_score DESC;")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[-1] for study_locations_tuple in study_locations_tuples]
    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()
    if variable in study_locations_list:
        c.execute("SELECT * FROM study_locations WHERE url_name = '{idf}'".format(idf=variable))
        data1 = c.fetchall()
        # data1 = c.execute("SELECT werkplek FROM study_locations WHERE werkplek = 'TU Delft Bibliotheek'")
        return render_template("modal.html", study_locations=variable, data=data1, column_names=column_names)
    else:
        return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True) 