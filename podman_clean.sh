podman rm --all
podman pod rm --all
podman rm --all
podman rmi --all

podman image ls --all
podman container ls --all
echo "[>] ALL CLEAR" | grep . --color
