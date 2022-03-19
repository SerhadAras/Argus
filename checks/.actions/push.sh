#!/bin/bash

DIRS="$(find . -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"

for DIR in $DIRS
do
    echo "#############################################"
    echo "Pushing $DIR"
    docker push ghcr.io/watcherwhale/checklist:$DIR-latest
done
