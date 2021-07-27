import urllib.request
import requests

#Getting Shopify Product URL
print("What is the Nike SNKRS products URL? (Please with https:// at the begining)")
url = input() 
print("------------------------")

#Getting Size
print("Please input the size You want. (In US Size e.g.: 9.5)")
size = input()
print("------------------------")

website = urlparse(url)
codelink = 'view-source:' + url
print('Processing...')


req = requests.get(url, 'html.parser')


