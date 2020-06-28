import settings
import tweepy
import dataset
from textblob import TextBlob
from datafreeze.app import freeze
import csv, json

db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()
freeze(result, format='csv', filename=settings.CSV_NAME)

cities = {}
with open('us_cities.csv') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for i, rows in enumerate(csvReader):
        city = rows['CITY']
        state = rows['STATE_NAME']
        cities[city] = state


data = {}
results = {}
with open('tweets.csv') as csvFile:
# with open('trump.csv') as csvFile:
# with open('biden.csv') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for i, rows in enumerate(csvReader):
        result = {}
        if not rows['user_location']:
            continue
        else:
            loc = rows['user_location'].split(',')
            for word in loc:
                if word in cities.keys():
                    if cities.get(word) != 'Puerto Rico' and cities.get(word) != 'District of Columbia':
                        result['id'] = float(rows['id'])
                        result['polarity'] = float(rows['polarity'])
                        result['text'] = rows['text']
                        state = cities.get(word)
                        result['user_location'] = state
                        result['subjectivity'] = float(rows['subjectivity'])
                        results.update({i: result})
                else:
                    continue
            
data['count'] = i + 1
data['results'] = results
data['meta'] = {}

with open('tweets.json', 'w') as jsonFile:
# with open('trump.json', 'w') as jsonFile:
# with open('biden.json', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))