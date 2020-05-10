FROM python:3-alpine

# tkinter is needed to run exercises that use the turtle module
RUN apk update && apk add python3-tkinter

WORKDIR /usr/src/app

# to keep container running until stopped
CMD tail -f /dev/null