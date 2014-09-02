FROM phusion/baseimage:0.9.13

# install system packages
RUN apt-get -qq update && apt-get -qy install ruby python-pip python-dev libpq-dev postgresql-client libsqlite3-dev git-core

# prepare directories
RUN mkdir /code
WORKDIR /code

# add code to image
ADD . /code/

RUN useradd plone -d /code -s /bin/bash
RUN python bootstrap.py
RUN bin/buildout -c dev.cfg
