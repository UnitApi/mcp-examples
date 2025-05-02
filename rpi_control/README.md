# Raspberry Pi Control (rpi_control)

This directory contains examples and scripts for controlling Raspberry Pi GPIO and hardware using the MCP Hardware Project.

## Installation

To install all dependencies on your Raspberry Pi (or remote machine), run:

```bash
bash install.sh
```

This will install Python dependencies and system packages required for GPIO and MCP hardware access.

## Usage

To install and start a demo client in one step:

```bash
bash start.sh
```

To run a specific example client:

```bash
bash client.sh
```
Edit `client.sh` to select which example to run (default: full_demo.py).

## Remote Installation

To install `rpi_control` on a remote Raspberry Pi (or any remote Linux machine) via SSH:

```bash
bash install_remote.sh user@remote_host [remote_path]
```
- `user@remote_host`: SSH target (e.g., pi@192.168.1.42)
- `[remote_path]`: (Optional) Path on remote (default: `~/rpi_control`)

This will:
1. Copy all files to the remote directory
2. Run `install.sh` on the remote

## Examples

- `examples/full_demo.py`: Complete workflow demo (LED control + audio recording)
- `audio_record.py`: Record audio using MCP Hardware Client
- `led_control.py`: Control an LED using MCP Hardware Client
- `mqtt_example.py`: Use MQTT bridge for MCP hardware access
- `rpi_control.py`: Advanced GPIO and hardware control (multiple demos)
- `hello_world.py`: Minimal test example

## File Overview

- `install.sh`: Install all dependencies (Python/system)
- `start.sh`: Install then run a demo client
- `client.sh`: Run a client example (edit to select)
- `install_remote.sh`: Copy and install rpi_control on a remote machine via SSH

## Requirements

- Raspberry Pi hardware
- MCP hardware package (see https://github.com/UnitApi/mcp-hardware)
- Python 3.7+

---

For more info, see the MCP Hardware Project: https://github.com/UnitApi/mcp-hardware