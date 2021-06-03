import urllib.request
import requests

#Getting Shopify Product URL
print("What is the Shopify products URL? (Please with https:// at the begining)")
url = input() 
print("------------------------")

#Getting Size
print("Please input the size You want. (In US Size e.g.: 9.5)")
size = input()
print("------------------------")

req = requests.get(url, 'html.parser')


