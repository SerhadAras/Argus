#!/bin/bash

DIRS="$(find . -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"
FAILED=0

for DIR in $DIRS
do
    echo "#############################################"
    echo "Running flow $DIR"
    docker run --rm ghcr.io/watcherwhale/checklist:$DIR-latest python /app/oneshot.py $@

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
