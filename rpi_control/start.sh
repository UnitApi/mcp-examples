#!/bin/bash
# start.sh: Run install.sh and start all example clients in examples/
set -e

dir="$(dirname "$0")"
cd "$dir"

bash install.sh

echo "[rpi_control] Running all examples in examples/ ..."

for example in examples/*.py; do
    echo "[rpi_control] Running $example ..."
    python3 "$example"
done
