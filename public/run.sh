#!/bin/bash

cd "$(dirname "$0")"

PORT=8080
IP=$(tailscale ip -4)

echo "Server available at http://$IP:$PORT/"

python3 -m http.server "$PORT" --bind 0.0.0.0 --directory ./public