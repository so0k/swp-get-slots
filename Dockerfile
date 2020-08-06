FROM python:3.8-buster
ENV TZ='Asia/Singapore'

WORKDIR /var/app/src
COPY requirements.txt /var/app/src/

RUN pip install -r /var/app/src/requirements.txt

COPY get_slots.py /var/app/src
ENTRYPOINT ["/var/app/src/get_slots.py"]
