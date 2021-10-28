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
    explanation_title = "Werkplekwijzer - Vind de beste werkplek bij jou in de buurt"
    explanation_body = "Een goede werkplek vinden buiten kantoor kan een uitdaging zijn. Werkplekwijzer beoordeelt werkplekken in Nederland op verschillende criteria zodat jij de beste werkplek kunt vinden. Wij maken scoreboards en delen ervaringen over werkplekken in jouw omgeving. Hiermee kan je op werkplekwijzer de beste keuze maken voor een werkplek buiten kantoor. Of je nu op zoek bent naar een café met de lekkerste koffie, of een werkplek met het snelste internet. Alle beoordelingen per werkplek zijn eenvoudig te vinden. Alle werkplekken zijn gratis en lopen uiteen van cafés tot bibliotheken. Ideaal als je een keer buiten kantoor wilt werken of een keer ergens anders wilt studeren dan thuis."

    title = "Werkplekwijzer - Vind de beste werkplek bij jou in de buurt"
    meta_description = "Een goede werkplek vinden buiten kantoor kan een uitdaging zijn. Werkplekwijzer beoordeelt werkplekken in Nederland op verschillende criteria zodat jij de beste werkplek kunt vinden."
    meta_keywords = "werkplek, werkplekwijzer, flexwerken, werkplekken, rotterdam, amsterdam, den haag, delft"
    meta_viewport = "width=960px"
    return render_template("home.html", title=title, meta_description=meta_description, meta_keywords=meta_keywords,
                           meta_viewport=meta_viewport, study_locations=study_locations_list, data=data,
                           column_names=column_names, explanation_title=explanation_title,
                           explanation_body=explanation_body)


@app.route("/den_haag")
def den_haag_filter():
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
    c.execute(f"SELECT * FROM study_locations WHERE stad='Den Haag' ORDER BY totale_score DESC")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations WHERE stad='Den Haag' ORDER BY totale_score DESC;")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[0] for study_locations_tuple in study_locations_tuples]
    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()
    explanation_title = "Beste werkplekken in Den Haag"
    explanation_body = "Werkplekwijzer zet de beste werkplekken in Den Haag voor je op een rijtje. De werkplekken zijn beoordeeld op verschillende criteria zodat jij gemakkelijk de beste werkplek kunt vinden. Den Haag is de hoofdstad van de provincie Zuid-Holland en is erg goed bereikbaar. De Nederlandse regering en het parlement bevinden zich in Den Haag. De stad is toeristisch en heeft twee bekende stranden: Scheveningen en Kijkduin. Daarnaast zijn er meerdere multinationals gevestigd in Den Haag zoals: Ahold, AEGON, ING Bank en KPN. Aan cafés met goede koffie is in Den Haag geen gebrek. Wij hebben voor jou de beste werkplekken in Den Haag uitgezocht."

    title = "Werkplekwijzer - Beste werkplekken in Den Haag"
    meta_description = "Werkplekwijzer zet de beste werkplekken in Den Haag voor je op een rijtje. De werkplekken zijn beoordeeld op verschillende criteria zodat jij de beste werkplek kunt vinden."
    meta_keywords = "werkplek, werkplekwijzer, flexwerken, werkplekken, rotterdam, amsterdam, den haag, delft"
    meta_viewport = "width=960px"
    return render_template("home.html", title=title, meta_description=meta_description, meta_keywords=meta_keywords,
                           meta_viewport=meta_viewport, study_locations=study_locations_list, data=data,
                           column_names=column_names, explanation_title=explanation_title,
                           explanation_body=explanation_body)


@app.route("/delft")
def delft_filter():
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
    c.execute(f"SELECT * FROM study_locations WHERE stad='Delft' ORDER BY totale_score DESC")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations WHERE stad='Delft' ORDER BY totale_score DESC;")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[0] for study_locations_tuple in study_locations_tuples]
    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()
    explanation_title = "Vind de beste werkplekken in Delft"
    explanation_body = "Delft"

    title = "Werkplekwijzer - Beste werkplekken in Delft"
    meta_description = "Op Werkplekwijzer vind je de beste werkplekken in Delft. Wij beoordelen alle werkplekken op de meest belangrijke criteria."
    meta_keywords = "werkplek, werkplekwijzer, flexwerken, werkplekken, rotterdam, amsterdam, den haag, delft"
    meta_viewport = "width=960px"
    return render_template("home.html", title=title, meta_description=meta_description, meta_keywords=meta_keywords,
                           meta_viewport=meta_viewport, study_locations=study_locations_list, data=data,
                           column_names=column_names, explanation_title=explanation_title,
                           explanation_body=explanation_body)


@app.route("/rotterdam")
def rotterdam_filter():
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
    c.execute(f"SELECT * FROM study_locations WHERE stad='Rotterdam' ORDER BY totale_score DESC")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations WHERE stad='Rotterdam' ORDER BY totale_score DESC;")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[0] for study_locations_tuple in study_locations_tuples]
    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()
    explanation_title = "Beste werkplekken in Rotterdam"
    explanation_body = "Werkplekwijzer heeft de beste werkplekken voor jou uitgezocht. We hebben de werkplekken in Rotterdam beoordeeld op belangrijke criteria zodat je eenvoudig de beste werkplekken kunt vinden. De stad Rotterdam heeft na Amsterdam het meeste aantal inwoners van Nederland. Rotterdam is bekend als havenstad en heeft de grootste haven van Europa. De Rotterdamse haven is een belangrijk logistiek en economisch centrum. Rotterdam is goed bereikbaar en heeft verschillende metrostations. Er zijn een hoop grote bedrijven te vinden zoals: Unilever, Nationale Nederlanden en Robeco. Ook aan werkplekken in Rotterdam zeker geen gebrek. Er zijn veel restaurants en cafés met lekkere koffie waar je wat kunt werken of studeren."

    title = "Werkplekwijzer - Beste werkplekken in Rotterdam"
    meta_description = "Werkplekwijzer heeft de beste werkplekken voor jou uitgezocht. We hebben de werkplekken in Rotterdam beoordeeld op belangrijke criteria zodat je eenvoudig de beste werkplekken kunt vinden."
    meta_keywords = "werkplek, werkplekwijzer, flexwerken, werkplekken, rotterdam, amsterdam, den haag, delft"
    meta_viewport = "width=960px"
    return render_template("home.html", title=title, meta_description=meta_description, meta_keywords=meta_keywords,
                           meta_viewport=meta_viewport, study_locations=study_locations_list, data=data,
                           column_names=column_names, explanation_title=explanation_title,
                           explanation_body=explanation_body)


@app.route("/amsterdam")
def amsterdam_filter():
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
    c.execute(f"SELECT * FROM study_locations WHERE stad='Amsterdam' ORDER BY totale_score DESC")
    data = c.fetchall()
    c.execute("SELECT werkplek FROM study_locations WHERE stad='Amsterdam' ORDER BY totale_score DESC;")
    # study_locations_tuples is a list of tuples, so for the location we only need the first element of each tuple
    study_locations_tuples = c.fetchall()
    study_locations_list = [study_locations_tuple[0] for study_locations_tuple in study_locations_tuples]
    # old query in which a single location is fetched
    # c.execute("SELECT total_score, price_consumptions_norm, access_hours_norm, google_review FROM study_locations "
    #           "where city = 'Delft'")
    # data = c.fetchall()
    explanation_title = "Beste werkplekken in Amsterdam"
    explanation_body = "Werkplekwijzer heeft de beste werkplekken voor jou uitgezocht. We hebben de werkplekken in Amsterdam beoordeeld op belangrijke criteria zodat je eenvoudig de beste werkplekken kunt vinden. De stad Rotterdam heeft na Amsterdam het meeste aantal inwoners van Nederland. Rotterdam is bekend als havenstad en heeft de grootste haven van Europa. De Rotterdamse haven is een belangrijk logistiek en economisch centrum. Rotterdam is goed bereikbaar en heeft verschillende metrostations. Er zijn een hoop grote bedrijven te vinden zoals: Unilever, Nationale Nederlanden en Robeco. Ook aan werkplekken in Rotterdam zeker geen gebrek. Er zijn veel restaurants en cafés met lekkere koffie waar je wat kunt werken of studeren."

    title = "Werkplekwijzer - Beste werkplekken in Amsterdam"
    meta_description = "Werkplekwijzer heeft de beste werkplekken voor jou uitgezocht. We hebben de werkplekken in Amsterdam beoordeeld op belangrijke criteria zodat je eenvoudig de beste werkplekken kunt vinden."
    meta_keywords = "werkplek, werkplekwijzer, flexwerken, werkplekken, rotterdam, amsterdam, den haag, delft"
    meta_viewport = "width=960px"
    return render_template("home.html", title=title, meta_description=meta_description, meta_keywords=meta_keywords,
                           meta_viewport=meta_viewport, study_locations=study_locations_list, data=data,
                           column_names=column_names, explanation_title=explanation_title,
                           explanation_body=explanation_body)


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