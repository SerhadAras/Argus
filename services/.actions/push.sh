#!/bin/bash

set -e

services=( "gateway" "sequencer" "cert-master" "metrics" )

for service in ${services[@]}
do

    if [ "$1" ];
    then
        REGISTRY="$1"
        docker tag $REGISTRY/$service:latest ghcr.io/watcherwhale/$service:latest
    fi

    VERSION="$(jq -r .version sequencer/package.json)"

    docker tag ghcr.io/watcherwhale/$service:latest ghcr.io/watcherwhale/$service:v$VERSION

    docker push ghcr.io/watcherwhale/$service:latest
    docker push ghcr.io/watcherwhale/$service:v$VERSION

done
