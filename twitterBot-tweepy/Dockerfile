FROM python:3-alpine

RUN pip install tweepy

WORKDIR /usr/src/app

# to keep container running until stopped
CMD tail -f /dev/null