#!/bin/bash

if [ -z "$1" ];
then
    REGISTRY="ghcr.io/watcherwhale"
else
    REGISTRY="$1"
fi

docker build --no-cache -f Dockerfile --build-arg service=gateway -t $REGISTRY/gateway .
docker build --no-cache -f Dockerfile --build-arg service=sequencer -t $REGISTRY/sequencer .
