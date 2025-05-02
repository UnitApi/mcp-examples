#!/bin/bash
# install.sh: Install dependencies for rpi_control on remote Raspberry Pi
set -e

echo "[rpi_control] Installing Python dependencies..."
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt || pip install -r requirements.txt
else
    echo "[rpi_control] No requirements.txt found, skipping pip install."
fi

echo "[rpi_control] Installing system packages..."
sudo apt-get update && sudo apt-get install -y python3-pip python3-dev python3-rpi.gpio

echo "[rpi_control] Installation complete."
