#!/usr/bin/python
#
# List buses due at a stop
#
import requests
from bs4 import BeautifulSoup
stopNo = 4123
stopUrl = "https://www.metlink.org.nz/stop/" + str(stopNo) + "/departures"

page = requests.get(stopUrl)
soup = BeautifulSoup(page.content, 'html.parser')

routes = soup.find_all('tr',class_=" ")
for i in range(len(routes)):
    stop_soup = BeautifulSoup(str(routes[i]), 'html.parser')
    next_route_id = stop_soup.find(class_="id-code-link").get_text().strip().ljust(4)
    next_route_name = stop_soup.find(class_="rt-destination-name").get_text().strip().ljust(16)
    next_route_time = stop_soup.find(class_= ["rt-service-time real", "rt-service-time"]).get_text().strip().rjust(8)  
    print( next_route_id, next_route_time , next_route_name)
