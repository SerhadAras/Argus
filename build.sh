#!/bin/bash

docker build -f docker/Dockerfile.gateway -t ghcr.io/watcherwhale/gateway .
docker build -f docker/Dockerfile.sequencer -t ghcr.io/watcherwhale/sequencer .