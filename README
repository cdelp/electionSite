# electionSite

This is the initial Django framework for an Election Information website being created for HACC. CSS and page templates were taken from Bootstrap.
Ignore all except for the electionSite folder

The project is "electionSite".
Within the "electionSite" folder, overall project changes can be made in the settings.py and urls.py files.

Within the "candidatesSite" folder, py files can be edited as needed.
"static" folder contains files needed for the web pages. These files are publically visible.
"templates/candidatesSite" folder contains the html pages. "home.html" is currently the main demo page. 
"header.html" is a template applied to all pages. "test.html" is a test page for navigation set-up.
* if adding more folders of html pages in templates, please add the appropriate info to "apps.py" and "views.py"

To access Hawaii Open Data Socrata database see this python example (change url as needed)
(requires "pip install requests" and "pip install sodapy")

import requests

url = "https://data.hawaii.gov/resource/u76e-fv4g.json?candidate_name=Bean, Tracy"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

for n, loop in enumerate(data):<br>
    print ("Record ", n)<br>
    print (data[n], '\n')

