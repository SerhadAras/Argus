#!/bin/bash

set -e

if [ "$1" ];
then
    REGISTRY="$1"

    docker tag $REGISTRY/gateway:latest ghcr.io/watcherwhale/gateway:latest
    docker tag $REGISTRY/sequencer:latest ghcr.io/watcherwhale/sequencer:latest
    docker tag $REGISTRY/cert-master:latest ghcr.io/watcherwhale/cert-master:latest
fi

GATEWAY_VERSION="$(jq -r .version sequencer/package.json)"
SEQUENCER_VERSION="$(jq -r .version sequencer/package.json)"
CERT_MASTER_VERSION="$(jq -r .version sequencer/package.json)"

docker tag ghcr.io/watcherwhale/gateway:latest ghcr.io/watcherwhale/gateway:v$GATEWAY_VERSION
docker tag ghcr.io/watcherwhale/sequencer:latest ghcr.io/watcherwhale/sequencer:v$SEQUENCER_VERSION
docker tag ghcr.io/watcherwhale/cert-master:latest ghcr.io/watcherwhale/cert-master:v$CERT_MASTER_VERSION

docker push ghcr.io/watcherwhale/gateway:latest
docker push ghcr.io/watcherwhale/sequencer:latest
docker push ghcr.io/watcherwhale/cert-master:latest

docker push ghcr.io/watcherwhale/gateway:v$GATEWAY_VERSION
docker push ghcr.io/watcherwhale/sequencer:v$SEQUENCER_VERSION
docker push ghcr.io/watcherwhale/cert-master:v$CERT_MASTER_VERSION
