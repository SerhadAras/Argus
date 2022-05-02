#!/bin/bash

set -e

if [ -z "$1" ];
then
    REGISTRY="ghcr.io/watcherwhale"
else
    REGISTRY="$1"
fi

docker build --no-cache -f Dockerfile -t $REGISTRY/checklist-scaler:latest .
