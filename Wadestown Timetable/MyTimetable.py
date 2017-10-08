#!/usr/bin/python
#
# Personal time table between two stops
#
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup

myStartStop ="4123"
myEndStop = "5510"
myStartDate = "2017-08-04"
myEndDate =   "2017-08-04"
##myStartTime = "00%3A00"
##myEndTime   = "23%3A55"
myStartTime = urllib.parse.quote("00:00")
myEndTime   = urllib.parse.quote("23:00")
myDays = "1"
myServiceCode = "14"

myUrl = ("https://www.metlink.org.nz/timetables/pocketinfo?" +
         "From=" + myStartStop + "&To=" + myEndStop + 
         "&StartDate=" + myStartDate + "&EndDate=" + myEndDate +
         "&StartTime=" + myStartTime   + "&EndTime=" + myEndTime +
         "&Days%5B%5D=" + myDays + "&ServiceCode=" + myServiceCode +
         "&action_doGenerateServiceInfo=View+my+Timetable" )
##myUrl = "https://www.metlink.org.nz/timetables/pocketinfo?From=4123&To=5510&StartDate=2017-08-04&EndDate=2017-08-04&StartTime=00%3A00&EndTime=23%3A00&Days%5B%5D=1&ServiceCode=14&action_doGenerateServiceInfo=View+my+Timetable"
##print(myUrl)

page = requests.get(myUrl)
soup = BeautifulSoup(page.content, 'html.parser')

journeyStartTimes = soup.find_all('tr', class_ = re.compile('first*'))
journeyEndTimes   = soup.find_all('tr', class_ = re.compile('last*'))

startSoup = BeautifulSoup(str(journeyStartTimes[1]), 'html.parser')
stopSoup  = BeautifulSoup(str(journeyEndTimes[1]),   'html.parser')

startTimes = startSoup.find_all('span',class_="timeValue")
stopTimes  =  stopSoup.find_all('span',class_="timeValue")
for i in range(len(startTimes)):
        print(startTimes[i].get_text().strip().rjust(10),
                stopTimes[i].get_text().strip().rjust(10))
   
