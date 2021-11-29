from bs4 import BeautifulSoup
import json
import requests


# domain
facts = 'https://www.factretriever.com'

#genrates request to domain stores response to result variable
result = requests.get(facts)

#empty dictionary to store results
results = {}

#Beautuful soup parses the html of the response and stores as text into our soup variable
soup = BeautifulSoup(result.text, "html.parser")

#loop over soup searching for links and text, storing our formatted results into our dictionary
for i, li in enumerate(soup.find_all('a', href=True)):
        if li.text != "":
            results[li.text.strip("\n\n")] = {"Link": 'https://www.factretriever.com' + li['href'] }

#create a file called facts.json and writes our results into our json file.
with open('facts.json', 'w') as json_file:
    json.dump(results, json_file)

# open json facts file
json_file = open('facts.json')

# load data in json format and make searchable
data = json.load(json_file)

#capture terminal input
search = str(input())

#print data if it exist
if data[search]: 
    print(data[search])

#closes file after completed search
json_file.close()