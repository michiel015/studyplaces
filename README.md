# Studyplaces [Deprecated] 
This is an outdated website that me and my friends used to run on werkplekwijzer.nl, aimed at ranking places to work/study at (e.g. cafes). We used Pieter Level's indie maker handbook MAKE as our guide to bootstrap this idea. Looking back on the technical side, there are a lot of things that we would have done differently, but this was our first prototype.

## How does it work?
We have a Google sheets in which we collect data (mostly by visiting or contacting places), you can view the data via this [link](https://docs.google.com/spreadsheets/d/1-lKEebAWQsylrN5uzjKaG3GlLfsFCnb-Tle1Wq23dqo/edit?usp=sharing). This data is then processed and missing information is interpolated. From the front_end tab in this file, a csv is exported and this csv is used to create an sqlite database using the functions in utilities.py. The Dash page is started by running main.py. 

We hosted this website using apache2 on a VPS running Ubuntu 18.04 LTS.

## Setup
Setup: install python 3.5> from the [Python homepage](https://www.python.org/downloads/). (I personally used an Anaconda environment and installed everything there)
Afterwards run:  
`pip install -r requirements.txt` in the repo folder.  
Website logic is contained in main.py, by running this file you can view the website at http://127.0.0.1:5000/ by default.  
