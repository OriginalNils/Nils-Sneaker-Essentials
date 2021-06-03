from urllib.request import urlopen
import requests
import xml.etree.ElementTree as ET
import urllib

#asking for shopify link
print("What is the Web Adress of the product? e.g.: https://eu.oneblockdown.it/products/ambush-dunk (Please with https:// infront)")

#getting shopify link
link = input()
print(link)
url = link +'.xml'
print(url)
response = urllib.request.urlopen(url).read()
#asking for output
print("Do you want the output in Discord Embed (1) or just normal the links (2)?")

#getting output info
output = input()
print(output)

#parsing
tree = ET.fromstring(response)
root = tree.getroot()

for sizecat in root.findall('variant'):
    id = sizecat.find('id').text
    size = sizecat.find('option1').text

    print(id, size)
