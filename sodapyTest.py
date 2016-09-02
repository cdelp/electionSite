# from api, using Python Requests
import requests

#url = "https://data.hawaii.gov/resource/u76e-fv4g.json"
url = "https://data.hawaii.gov/resource/u76e-fv4g.json?candidate_name=Bean, Tracy"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

for n, loop in enumerate(data):
    print ("Record ", n)
    print (data[n], '\n')
