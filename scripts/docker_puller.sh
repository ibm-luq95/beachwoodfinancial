#!/usr/bin/env zsh
set -o errexit
set -o pipefail
set -o nounset

echo "Pulling latest docker images for beachwood..."
echo "Pulling Python:3.13-bookworm..."
docker pull python:3.13-bookworm
echo "**********************************************************"
echo "Pulling Postgres alpine..."
docker pull postgres:alpine
echo "**********************************************************"
#echo "Pulling Valkey (Redis alternative)..."
#docker pull valkey/valkey
echo "**********************************************************"
echo "Pulling Nginx..."
docker pull nginx:latest
echo "**********************************************************"
echo "Pulling Cloudflare..."
docker pull cloudflare/cloudflared:latest
echo "**********************************************************"

notify-send "Docker images pulled successfully"
