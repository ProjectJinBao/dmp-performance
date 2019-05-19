#!/bin/bash
config=`cat ./config`
templ=`cat ../../docker-compose-template.yml`
printf "$config\ncat << EOF\n$templ\nEOF" | bash > ./docker-compose.yml

docker-compose up -d