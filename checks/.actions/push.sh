#!/bin/bash

set -e

DIRS="$(find . -maxdepth 1 -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"

if [ "$1" ];
then
    REGISTRY="$1"
fi

for DIR in $DIRS
do
    echo "#############################################"

    if [ "$REGISTRY" ];
    then
        echo "Retagging $DIR"
        docker tag $REGISTRY/checklist:$DIR-latest ghcr.io/watcherwhale/checklist:$DIR-latest
    fi

    echo "Pushing $DIR"
    docker push ghcr.io/watcherwhale/checklist:$DIR-latest
done
