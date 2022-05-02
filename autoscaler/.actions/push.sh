#!/bin/bash

set -e

VERSION=$(cat VERSION)

if [ "$1" ];
then
    REGISTRY="$1"
    docker tag $REGISTRY/checklist-scaler:latest ghcr.io/watcherwhale/checklist-scaler:latest
fi

docker tag ghcr.io/watcherwhale/checklist-scaler:latest ghcr.io/watcherwhale/checklist-scaler:v$VERSION

docker push ghcr.io/watcherwhale/checklist-scaler:latest
docker push ghcr.io/watcherwhale/checklist-scaler:v$VERSION
