#!/usr/bin/env bash

sudo docker run \
  --rm -ti -d \
  --name l_dropper \
  -v $PWD/files/:/app/files \
  -p 0.0.0.0:8080:80 \
  dropper
