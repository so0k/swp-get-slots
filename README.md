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
