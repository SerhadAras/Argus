#!/bin/bash

set -e

DIRS="$(find . -maxdepth 1 -type d -not -path ./.actions | tail -n +2 | sed -e "s/\.\///g")"

for DIR in $DIRS
do
    cd $DIR
    echo $DIR
    npm i
    cd ..
done
