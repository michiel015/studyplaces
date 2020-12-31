# -*- coding: utf-8 -*- 
# __author__: Adarsh Kalikadien #
import sqlite3
import pandas as pd


def convert_csv_to_sqlite_db(csv_filename):
    '''Convert CSV files to SQLITE3 database, the script assumes that the CSV file and database are
    in the same folder as the script

    :param csv_filename:
    :return: SQLITE3 database with contents from CSV file
    '''
    db_filename = csv_filename.split('.')[0]
    conn = sqlite3.connect(db_filename + '.db')
    location_csv = pd.read_csv('test.csv')  # load in dataframe
    # create table study_locations in test.db
    location_csv.to_sql('study_locations', conn, if_exists='replace', index=False)


if __name__ == "__main__":
    convert_csv_to_sqlite_db('test.csv')
