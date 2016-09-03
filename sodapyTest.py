# from api, using Python Requests
import requests
import json

#url = "https://data.hawaii.gov/resource/u76e-fv4g.json"
#url = "https://data.hawaii.gov/resource/u76e-fv4g.json?candidate_name=Bean, Tracy"
#url = "https://data.hawaii.gov/resource/u76e-fv4g.json?noncandidate_committee_name=ActBlue Hawaii"

# lists candidate name and amount for all contributions > $5000 made by ActBlue Hawaii after 1/1/2014
#url = "https://data.hawaii.gov/resource/u76e-fv4g.json?$query=SELECT noncandidate_committee_name, candidate_name, amount WHERE amount > 5000 AND noncandidate_committee_name = 'ActBlue Hawaii' AND date > '2014-01-01T12:01:00'"

# 2016 contributors (individual contributions over $3000) in descending order.
url = "https://data.hawaii.gov/resource/u76e-fv4g.json?$query=SELECT noncandidate_committee_name, amount WHERE amount > 3000 AND date > '2016-01-01T12:01:00' ORDER BY amount DESC"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

# list on contributors, filled below
contrib_list = list()

# print records as strings
for d in data:
    json_string = json.dumps(d)
    parsed_json = json.loads(json_string)
    #print ("JSON string", json_string)
    com_name = parsed_json['noncandidate_committee_name']

    # adds contributor's name to list if not already in it
    for i in data:       
        if com_name not in contrib_list:
            print("adding to list")
            contrib_list.append(com_name)    

# print records as list
for n, loop in enumerate(data):
    print ("Record ", n)
    print (data[n], '\n')

# prints list of contributors
for name in contrib_list:
    print(name)
