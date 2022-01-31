import requests, json


url2 = "https://api.opencovid.ca/other?stat=prov"
response2 = requests.get(url2)
covid2 = json.loads(response2.text) 


for facts in covid2["prov"]:
    if(facts["pop"] != "NULL"):
        print("{}: {:,.0f}".format(facts["province"],facts["pop"]))
    print("\n")