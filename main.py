import requests
from pprint import pprint

def getlocs():
    print("Getting Train Locations...")

    headers = {
        'authority': 'anytrip.com.au',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    response = requests.get('https://anytrip.com.au/api/v3/region/au3/vehicles?feeds=au3:ab', headers=headers)
    trains = {}
    allcars = {}
    for trainobj in response.json()['response']['vehicles']:
        trains[trainobj['vehicleInstance']['id']] = trainobj['vehicleInstance']['lastPosition']['statusString']

    for train, location in trains.items():

        cars = train.split('-')
        for i in cars:
            allcars[i] = location
    return allcars

def main():
    print('''
  __  __      _               _______        _             _______             _             
 |  \/  |    | |             |__   __|      (_)           |__   __|           | |            
 | \  / | ___| |_ _ __ ___      | |_ __ __ _ _ _ __  ___     | |_ __ __ _  ___| | _____ _ __ 
 | |\/| |/ _ \ __| '__/ _ \     | | '__/ _` | | '_ \/ __|    | | '__/ _` |/ __| |/ / _ \ '__|
 | |  | |  __/ |_| | | (_) |    | | | | (_| | | | | \__ \    | | | | (_| | (__|   <  __/ |   
 |_|  |_|\___|\__|_|  \___/     |_|_|  \__,_|_|_| |_|___/    |_|_|  \__,_|\___|_|\_\___|_|   
                                                                                             
                                                                                                                   
By Dom Is Offline#0001\n''')
    carlist = getlocs()
    train_input = input("Enter car number:\n")
    if train_input in carlist:
        print("Your requested car is", carlist[train_input] + "!")
    else:
        print("Your requested car is not currently being tracked or is not a valid car number!")

if __name__ == "__main__":
    main()