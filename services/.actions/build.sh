#!/bin/bash

docker build --no-cache -f Dockerfile --build-arg service=gateway -t ghcr.io/watcherwhale/gateway .
docker build --no-cache -f Dockerfile --build-arg service=sequencer -t ghcr.io/watcherwhale/sequencer .
