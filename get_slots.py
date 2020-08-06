#!/usr/bin/env python

import sys, getopt, time
from datetime import date, datetime, timedelta
import requests
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

dateFormat = '%A, %b %d %Y'

def main(argv):
    help='get_slots.py -s <swpsystema|swpsystemb|swpsystemc> -d <date:YYYY-MM-DD>'
    
    startDate = date.today()
    maxDate = date.today() + timedelta(days=14)
    system = 'swpsystemc'

    try:
       opts, args = getopt.getopt(argv,"hs:d:",["system=","date="])
    except getopt.GetoptError:
       print(help)
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print(help)
          sys.exit()
       elif opt in ("-s", "--system"):
          system = arg
       elif opt in ("-d", "--date"):
          startDate = date.fromisoformat(arg)
    
    # prepare for first fetch
    jumpDate = startDate
    toDate = startDate + timedelta(days=6)
    if toDate > maxDate:
        toDate = maxDate

    while jumpDate <= maxDate:
        print("Fetching available slots for {system} from {fromDate} to {toDate}:".format(
                system=system,
                fromDate=jumpDate.strftime(dateFormat),
                toDate=toDate.strftime(dateFormat))
            ,end='\n'*2)
        fetchSlots(system,jumpDate)

        # prepare for next fetch
        jumpDate = jumpDate + timedelta(days=7)
        toDate = jumpDate + timedelta(days=6)
        if toDate > maxDate:
            toDate = maxDate
        time.sleep(2) # sleep 2 seconds

def fetchSlots(system,jumpDate):
    baseURL="https://{calendar}.youcanbook.me"
    query="/service/jsps/cal.jsp?cal={calendarId}&ini={calendarIni}&service={calendarService}&jumpDate={jumpDate}"

    calendars = {
        "swpsystemb": {
            "id": "21617379-33ba-41d3-b341-50b7fac01693",
            "ini": "1596626159288",
            "service": "jsid21231"
        },
        "swpsystemc": {
            "id": "693eae8c-0144-407d-92f2-725867e5be04",
            "ini": "1596625182764",
            "service": "jsid8744009"
        },
    }

    calendar = calendars[system]
    page = requests.get(
        baseURL.format(calendar = system) + query.format(
            calendarId = calendar["id"],
            calendarIni = calendar["ini"],
            calendarService = calendar["service"],
            jumpDate = str(jumpDate)
        )
    )

    soup = BeautifulSoup(page.content, 'html.parser')

    body = soup.find(id='body')
    day_elems = body.select("div.gridDay") # find_all('div', class_='gridPage')
    for day_elem in day_elems:
        free_elems = day_elem.select("div.gridSlot.gridFree")
        for free_elem in free_elems:
            link = free_elem.find('a')
            url = baseURL.format(calendar = system) + link['href']
            qs = parse_qs(urlparse(url).query)
            slot = datetime.fromtimestamp(int(qs["slot"][0])/1000)
            
            print(slot.strftime(dateFormat)+" "+link.text.strip()+" "+ url, end='\n'*2)

if __name__ == "__main__":
   main(sys.argv[1:])
