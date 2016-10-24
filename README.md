# Schengen_1
This tool observes the change in internet routing by conducting traceroutes for targets in Europe. 

##Working
The web interface communicates with RIPE Atlas through Cousteau, a Python client for
RIPE Atlas API. RIPE Atlas is a global network of probes that measure Internet connectivity and reachability, used here to conduct measurements and obain the corresponding results. The website consists of a single application called ”measurement”. This application lets the user start a new measurement, stop a measurement and analyse the results from currently running
measurements. MySQL is chosen for database management.<br />
The user is required to fill forms on the web interface. The forms conisist of ”specification” which
includes the interval, protocol and duration data; ”probes” which includes country and number
of probes from each country. All this data gets saved in the database when a form is submitted
and validated. Then finally the user can start a measurement by specifying the target that is by
entering the hostname or IP address, description and then selecting the probes and specification
from the options available in the database (prefilled).<br />
Whenever a new measurement is initialised an ID(msm id) is obtained from RIPE Atlas through
the API as a response to a successful create measurement request. This ID is also saved in the
database and is used to identify the measurements later on. The requirement of identification of
a measurement could be for purpose of stopping the measurement or for analysing the results.<br />
The database consists of tables "Specification", "Probes , "Target" for storing information about the measurements ; "Countries", "Traceroutemeasurement*number*", "Relation*number*" for storing the data obtained for each measurement, where the number corresponds to the number of the measurement mentioned in its description. Therefore, each measurement has two tables for itself.

                     

##Features
A lot can be done with the observed data in the database by tweaking the code a bit for every new feature.
Currently, the user can mention the required time period as well as the country for any measurement to observe the graph for that particular country , showing the change in percentage of IP addresses that were part of the traceroute path for the measurement.<br />
There fore, by observing this over a long period a pattern might become visible or any change observed can be attributed to a cause.

##Technologies
Server-side

    Python 2.7+: The language of choice.
    Django: Web framework written in Python, used to serve all pages.
    MySQL: Relational database, used to store measurement data and specifications.
    

Client-side and design

    Google charts: Google chart API used for displaying graphs.
    
##Installation Instructions
**Prerequisite**: Apache, Django

**Installing on Linux/Ubuntu**


    1.Database set up and connection to Django.MySql connector- https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-notes.
    2. RIPE Atlas API and parsing library
        pip install ripe.atlas.cousteau
        pyOpenSSL-Sagan dependency
        pip install ripe.atlas.sagan
    3. Google charts:
        pip install django-google-charts
        pip install django-qsstats-magic
    4. Maxmind database:
        pip install geoip2
        For updating the database every week: sudo add-apt-repository ppa:maxmind/ppa
        sudo apt update
        sudo apt install geoipupdate
        follow the steps in- http://dev.maxmind.com/geoip/geoipupdate/
    5. django-cron:
        pip install django_cron
        

##Usage
For using the tool, API key is required for the corresponding account in RIPE Atlas through which the measurements have to be created, it is needed for both starting and stopping measurements.
