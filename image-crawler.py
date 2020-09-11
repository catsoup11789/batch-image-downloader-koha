import urllib.request
import csv

print('Ready to work.')

# start with a csv file with unique identifiers for each image
with open('cardnumbers.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    cardnumbers = []
    for row in readCSV:
        cardnumber = row[0]
        cardnumbers.append(cardnumber)
        
for id in cardnumbers: 
    # path to find images, minus the unique identifier
    url = 'url that prefixes image location'+id
    
    # path to download images to
    urllib.request.urlretrieve(url, '/Users/username/Downloads/images/'+id+'.jpg')
    
print('Jobs done.')