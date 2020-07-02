#!/bin/sh
# removes pods and containers
podman kill -a
podman rm -a
podman pod rm -a
podman rm -a
echo '[>] done'
