import requests, json

url = "https://api.opencovid.ca/"#
response = requests.get(url)

covid = json.loads(response.text)

for facts in covid["summary"]:
    for key, value in facts.items():
        print("{}: {:,.0f}".format(key,value))
print("version " + covid["version"])



