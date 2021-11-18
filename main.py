# __author__: Adarsh Kalikadien #
import sqlite3
from flask import Flask, render_template, url_for
from flask_sitemap import Sitemap
import socket
import datetime

from utilities import *
app = Flask(__name__)
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True
app.config['SITEMAP_IGNORE_ENDPOINTS'] = ['sitemap.xml', 'robot', 'test1']
ext = Sitemap(app=app)


hostname = socket.gethostname()

    @@ -231,10 +225,9 @@ def test1():
    return render_template("test1.html")


# ToDo: delete in next commit after verifying dynamic sitemap generation
# @app.route("/sitemap.xml")
# def sitemap():
#     return render_template("sitemap.xml")


@app.route("/robot.txt")
    @@ -284,43 +277,5 @@ def location_page(variable):
        return render_template("404.html")


@ext.register_generator
def sitemap():
    """Dynamically create a sitemap
    The 'SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS' parameter takes care of the static pages.
    For the dynamic pages we iterate over all study locations contained in the dataset, which will be the 'variable'
    in the dynamic location_page function.
    :return:
    """

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

    for study_location in study_locations_list:
        now = datetime.datetime.now()
        # function, variable: dynamic value, LastMod, Updatefrequency, priority
        yield 'location_page', {'variable': study_location}, f"{now.year}-{now.month}", 'monthly', 0.80


if __name__ == "__main__":
    app.run(debug=True) 