#!/bin/sh
watch -n 1 -t "podman image ls --all &&
echo '----------------------------------------------------------------------' &&
podman container ls --all "
