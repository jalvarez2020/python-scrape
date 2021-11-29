from ast import Num, Str
from bs4 import BeautifulSoup
import json
import requests



rinos = 'https://www.factretriever.com'
musk = 'https://en.wikipedia.org/wiki/Elon_Musk'

results = {}

result = requests.get(rinos)
soup = BeautifulSoup(result.text, "html.parser")
for i, li in enumerate(soup.find_all('a', href=True)):
        results[i] = {"Fact":  li.text.strip("\n\n"), "Link": 'https://www.factretriever.com' + li['href'] }

# headers = [header for header in doc.find_all("a", href=True)]
# links = [header.li for header in doc.find("li", {"class": "toclevel-1"})]

# for content in tesla:
#     tesla_results[content.li] = content.a
# result_json = json.dumps(results)
with open('facts.json', 'w') as json_file:
    json.dump(results, json_file)

print(results)