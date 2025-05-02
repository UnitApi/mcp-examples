#!/bin/bash
# client.sh: Run a client example
set -e

dir="$(dirname "$0")"
cd "$dir"

# Choose which example to run
python3 examples/full_demo.py
# python3 audio_record.py
# python3 led_control.py
# python3 mqtt_example.py
# python3 rpi_control.py
