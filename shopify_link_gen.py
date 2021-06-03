import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#Getting Shopify Product URL
print("What is the Shopify products URL? (Please with https:// at the begining)")
url = input() 
print("------------------------")

#Getting Quantity
print("What Quantity do you want? (At hyped items mostly a Quantaty of 1 is max)")
quantity = input()
print("------------------------")

#Getting Size
print("Please input the size You want. (In the format like on the website.)")
size = input()
print("------------------------")

#build xml link
website = urlparse(url)
baseurl = 'https://'+website.netloc+'/cart/'
xml = url+'.xml'
print('Processing...')

#parse variant
xmlopen = urllib.request.urlopen(xml).read()
soup = BeautifulSoup(xmlopen, 'xml')
try:
    variant = soup.find(text=size).findPrevious('id').text
    print('variant {} found for size {}'.format(variant, size))

except AttributeError:
    print('Attribute Error: size could not be found')

#build BD link
try:
    BD = baseurl+variant+':'+quantity
    print('succesfully created backdoor link: {}'.format(BD))
    
except NameError:
     print('Name Error: size could not be found')

print("------------------------")
k=input("press close to exit") 
