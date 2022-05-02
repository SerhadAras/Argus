#!/bin/bash

set -e

services=( "gateway" "sequencer" "metrics" )

if [ -z "$1" ];
then
    REGISTRY="ghcr.io/watcherwhale"
else
    REGISTRY="$1"
fi

for service in ${services[@]}
do
    docker build --no-cache -f Dockerfile --build-arg service=$service -t $REGISTRY/$service .
done

docker build --no-cache -f Dockerfile.cert --build-arg service=cert-master -t $REGISTRY/cert-master .
