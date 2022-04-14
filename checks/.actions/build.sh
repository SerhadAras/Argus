#!/bin/bash

set -e

DIRS="$(find . -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"

if [ -z "$1" ];
then
    REGISTRY="ghcr.io/watcherwhale"
else
    REGISTRY="$1"
fi

for DIR in $DIRS
do
    echo "#############################################"
    echo "Building flow $DIR"
    docker build --no-cache -f Dockerfile --build-arg checklist=$DIR --build-arg registry=$REGISTRY -t $REGISTRY/checklist:$DIR-latest .
done
