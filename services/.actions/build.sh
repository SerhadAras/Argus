#!/bin/bash

set -e

if [ -z "$1" ];
then
    REGISTRY="ghcr.io/watcherwhale"
else
    REGISTRY="$1"
fi

docker build --no-cache -f Dockerfile --build-arg service=gateway -t $REGISTRY/gateway .
docker build --no-cache -f Dockerfile --build-arg service=sequencer -t $REGISTRY/sequencer .
docker build --no-cache -f Dockerfile.cert --build-arg service=cert-master -t $REGISTRY/cert-master .
