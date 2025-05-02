#!/bin/bash
# install.sh: Install dependencies for rpi_control on remote Raspberry Pi
set -e

# Step 0: Upgrade pip to latest version
python3 -m pip install --upgrade pip || pip install --upgrade pip

echo "[rpi_control] Installing Python dependencies..."
# Step 1: Upgrade pip and install Cython first
pip3 install --upgrade pip || pip install --upgrade pip
pip3 install Cython || pip install Cython

# Step 2: Install all requirements except unitmcp
if [ -f requirements.txt ]; then
    # Install all except unitmcp
    grep -v '^unitmcp' requirements.txt > requirements_no_unitmcp.txt
    pip3 install -r requirements_no_unitmcp.txt --upgrade || pip install -r requirements_no_unitmcp.txt --upgrade
else
    echo "[rpi_control] No requirements.txt found, skipping pip install."
fi

# Step 3: Install unitmcp separately for best dependency resolution
pip3 install unitmcp || pip install unitmcp

# Step 4: Install pyjnius from GitHub to fix .pxi error
pip3 install git+https://github.com/kivy/pyjnius.git || pip install git+https://github.com/kivy/pyjnius.git

echo "[rpi_control] Installing system packages..."
sudo apt-get update && sudo apt-get install -y python3-pip python3-dev python3-rpi.gpio

echo "[rpi_control] Installation complete."
