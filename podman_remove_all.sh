#!/bin/sha
# fully removes podman images, pods and containers
podman kill -a
podman rm -a
podman pod rm -a
podman rm -a
podman rmi -a
echo '[>] DONE --------------------------'
