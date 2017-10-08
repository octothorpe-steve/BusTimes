#!/usr/bin/python
# import the library
from appJar import gui
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re

resultMessage = ""


# create a GUI variable called app
app = gui()

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Buses due")
app.setLabelBg("title", "#af3412")
app.addLabel("dateTime", datetime.now().strftime("%d. %B %Y %H:%M "))
app.setLabelBg("dateTime", "#CECECE")

#app.addLabelEntry("Bus Stop No.")
#app.setEntry ( "Bus Stop No.", 4123 )

app.addLabelOptionBox("Bus Stop No.", ["4123 Wadestown Shops", "5000 Courtney Place", "5006 Manners Street",
                        "5008 Willis Street", "5111 Molesworth"])


app.addMessage("timetable"," ")
#app.addGrid("routeGrid",[[ "Route", "Destination", "Time"]], addRow="True")

def press(button):
    resultMessage = ""
    if button == " Cancel ":
        app.stop()
    else:
        myStop = app.getOptionBox("Bus Stop No.")[:4]
        stopUrl = "https://www.metlink.org.nz/stop/" + str(myStop) + "/departures"
        #print(stopUrl)
        page = requests.get(stopUrl)
        soup = BeautifulSoup(page.content, 'html.parser')

        routes = soup.find_all('tr',class_=[" ",  re.compile('active*')])
        for i in range(len(routes)):
            stop_soup = BeautifulSoup(str(routes[i]), 'html.parser')
            next_route_id = stop_soup.find(class_="id-code-link").get_text().strip().ljust(6)
            next_route_name = stop_soup.find(class_="rt-destination-name").get_text().strip().ljust(18)
            next_route_time = stop_soup.find(class_= ["rt-service-time real", "rt-service-time"]).get_text().strip().ljust(12)  
            #print( next_route_id, next_route_time , next_route_name)
            resultMessage = resultMessage + next_route_id  + next_route_name + next_route_time + "\n"
            
            #app.addGridRow("routeGrid", [next_route_id, next_route_name, next_route_time])
        
            # Display the timetable
        app.setMessage("timetable", resultMessage)
        app.getMessageWidget("timetable").config(font="Courier 11")
        
        app.setLabel("dateTime", datetime.now().strftime("%d. %B %Y %H:%M "))



# link the buttons to the function called press
app.addButtons([" Update ", " Cancel "], press)

# start the GUI
app.go()
