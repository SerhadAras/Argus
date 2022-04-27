#!/bin/bash

DIRS="$(find . -maxdepth 1 -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"
FAILED=0

if [ -z "$2" ];
then
    REGISTRY="ghcr.io/watcherwhale"
else
    REGISTRY="$2"
fi

for DIR in $DIRS
do
    echo "#############################################"
    echo "Running flow $DIR"
    docker run --rm $REGISTRY/checklist:$DIR-latest python /app/oneshot.py $@

    if [ "$?" != "0" ];
    then
        echo ""
        echo "/!\\ $DIR flow failed /!\\"
        FAILED=1
    fi
done

if [ "$FAILED" == "1" ];
then
    echo "#############################################"
    echo ""
    echo "/!\\ Some or all flows have failed! /!\\"

    exit 1
fi
