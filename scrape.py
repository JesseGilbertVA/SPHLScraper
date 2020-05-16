#Importing Modules.
import requests
import sys
import csv
import os
import pyinputplus as pyip
from bs4 import BeautifulSoup
from datetime import date

#Get today's date and convert it to a string.
today_raw = date.today()
today = today_raw.strftime('%m_%d_%Y')

print('Welcome to the SPHL 2019-20 stats exporter made by Jesse Gilbert!')

#Links for 2019-20 SPHL season stats:
urls = ['http://stats.pointstreak.com/teamplayerstats.html?teamid=668983&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=626972&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=24908&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=24909&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=24911&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=570025&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=207820&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=456971&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=718716&seasonid=19674',
        'http://stats.pointstreak.com/teamplayerstats.html?teamid=626973&seasonid=19674']

#Ask user to select which team they'd like to export stats for.
response = pyip.inputMenu(['Birmingham Bulls', 'Evansville Thunderbolts', 'Fayetteville Marksmen', 'Huntsville Havoc', 'Knoxville Ice Bears', 
'Macon Mayhem', 'Pensacola Ice Flyers', 'Peoria Rivermen', 'Quad City Storm', 'Roanoke Rail Yard Dawgs'], numbered=True)

print('You selected: ' + response)
print('Generating .csv file...')

#Select URL for scraping based on user input.
if response == 'Birmingham Bulls':
    url = urls[0]
elif response == 'Evansville Thunderbolts':
    url = urls[1]
elif response == 'Fayetteville Marksmen':
    url = urls[2]
elif response == 'Huntsville Havoc':
    url = urls[3]
elif response == 'Knoxville Ice Bears':
    url = urls[4]
elif response == 'Macon Mayhem':
    url = urls[5]
elif response == 'Pensacola Ice Flyers':
    url = urls[6]
elif response == 'Peoria Rivermen':
    url = urls[7]
elif response == 'Quad City Storm':
    url = urls[8]
elif response == 'Roanoke Rail Yard Dawgs':
    url = urls[9]

#Begin scraping
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.findAll('table')
players = table[0]
goalies = table[1]

player_rows = players.findAll('tr')
goalie_rows = goalies.findAll('tr')

#CSV Headers
player_headers = ['NUMBER', 'PLAYER', 'POS', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PP', 'PPA', 'SH', 'SHA', 'GWG', 'SHOTS', 'S%']
goalie_headers = ['NUMBER', 'GOALIES', 'GP', 'MIN', 'W,', 'L', 'OTL', 'SOL', 'SO', 'GA', 'GAA', 'SV', 'SV%']

#Create file name
filename = response + " Export " + today + '.csv' 

#Create CSV
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(player_headers)
    for pr in player_rows:
        pd = pr.findAll('td')
        prow = [ip.text.strip() for ip in pd]
        if any(prow):
            csvwriter.writerow(prow)

    csvwriter.writerow(goalie_headers)
    for gr in goalie_rows:
        gd = gr.findAll('td')
        grow = [ig.text.strip() for ig in gd]
        if any(grow):
            csvwriter.writerow(grow)


input('Done! Press enter to exit.')