FROM python:3.7-alpine
MAINTAINER  @iqdavidh

ENV PYTHONUNBUFFERED 1
ENV VARTEST YEABABY

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client

#LA opcion virtual nos permite aagregar dependedncias temporales que necesimost
#para ejecutar la compilacion de postgress
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

#Borramos las dependencias que tenamos de compilacion
RUN apk del .tmp-build-deps

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
