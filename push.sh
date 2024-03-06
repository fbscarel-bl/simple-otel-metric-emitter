#!/usr/bin/env sh
docker buildx build --platform linux/amd64,linux/arm64 --tag fbscarelbl/simple-otel-metric-emitter:latest --push .
