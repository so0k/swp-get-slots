# SWP - Get Slots

Python script to fetch available slots for Singapore Wake Park

build docker image:

```
docker build -t swp-get-slots .
```

Run docker image:

```
$ docker run -it swp-get-slots -h
get_slots.py -s <swpsystema|swpsystemb|swpsystemc> -d <date:YYYY-MM-DD>
```

Example output:

```
11:11:54 vincentdesmet@ip-192-168-1-50 ~/personal/swp-get-slots 
$ docker run -it swp-get-slots -s swpsystemb
Fetching available slots for swpsystemb from Friday, Aug 07 2020 to Thursday, Aug 13 2020:

Friday, Aug 07 2020 8:00 PM https://swpsystemb.youcanbook.me/service/jsps/book.jsp?cal=21617379-33ba-41d3-b341-50b7fac01693&ini=1596626159288&service=jsid21231&jumpDate=2020-08-07&slot=1596801600000

Fetching available slots for swpsystemb from Friday, Aug 14 2020 to Thursday, Aug 20 2020:

Friday, Aug 14 2020 10:00 AM https://swpsystemb.youcanbook.me/service/jsps/book.jsp?cal=21617379-33ba-41d3-b341-50b7fac01693&ini=1596626159288&service=jsid21231&jumpDate=2020-08-14&slot=1597370400000

Fetching available slots for swpsystemb from Friday, Aug 21 2020 to Friday, Aug 21 2020:

Friday, Aug 21 2020 10:00 AM https://swpsystemb.youcanbook.me/service/jsps/book.jsp?cal=21617379-33ba-41d3-b341-50b7fac01693&ini=1596626159288&service=jsid21231&jumpDate=2020-08-21&slot=1597975200000
```
