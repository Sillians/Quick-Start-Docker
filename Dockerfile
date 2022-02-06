FROM python:3.8-slim-buster

ADD main.py .

RUN pip3 install requests beautifulsoup4

CMD [ "python3" "./main.py" ]