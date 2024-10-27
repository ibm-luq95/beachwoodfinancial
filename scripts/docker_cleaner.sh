#!/usr/bin/env zsh
set -o errexit
set -o pipefail
set -o nounset

echo "Cleaning docker images related to beachwood..."
echo "Deleting containers..."
docker rmi beachwoodfinancial_development_webapp
docker rmi beachwoodfinancial_development_db
docker rmi beachwoodfinancial_development_cache
docker rmi beachwoodfinancial_development_cloudflaretunnel

echo "Deleting volumes"
docker volume rm beach_wood_financial_mediafiles beach_wood_financial_pgdata beach_wood_financial_staticfiles
