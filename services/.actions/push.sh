#!/bin/bash

if [ "$1" ];
then
    REGISTRY="$1"

    docker tag $REGISTRY/gateway:latest ghcr.io/watcherwhale/gateway:latest
    docker tag $REGISTRY/sequencer:latest ghcr.io/watcherwhale/sequencer:latest
    docker tag $REGISTRY/cert-master:latest ghcr.io/watcherwhale/cert-master:latest
fi

docker push ghcr.io/watcherwhale/gateway:latest
docker push ghcr.io/watcherwhale/sequencer:latest
docker push ghcr.io/watcherwhale/cert-master:latest