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

## .env Configuration

All Python and shell scripts in this project use a `.env` file for configuration.

- Copy `env.sample` to `.env` and edit as needed:
  ```bash
  cp env.sample .env
  ```
- Set variables such as:
  - `RPI_HOST`, `RPI_USERNAME`, `RPI_PORT`: Raspberry Pi connection info for Python examples
  - `REMOTE`, `REMOTE_PATH`: Used by `install_remote.sh` for remote installation
  - `SCRIPT_DIR`: Used by `start.sh` and `client.sh` to set the working directory

**Example .env:**
```ini
RPI_HOST=raspberrypi
RPI_USERNAME=pi
RPI_PORT=8080
REMOTE=pi@raspberrypi
REMOTE_PATH=~/pi
SCRIPT_DIR=./rpi_control
```

All examples and shell scripts will automatically use these variables.

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
- `examples/play_audio_unitmcp.py`: Play a .wav or .mp3 file on the remote device using MCP Hardware Client
- `examples/speaker_control.py`: Play a .wav or .mp3 file locally (requires speaker output)

## Audio Playback on Remote Device

You can play audio files on the remote Raspberry Pi using the MCP Hardware Client:

```bash
python3 examples/play_audio_unitmcp.py --file examples/test.wav
```

If you do not specify `--file`, the script will use the defaults set in your `.env` file (`DEFAULT_WAV` or `DEFAULT_MP3`).

Example `.env` entries:
```
DEFAULT_MP3=test.mp3
DEFAULT_WAV=test.wav
```

To play audio locally (on the device running the script) instead, use:

```bash
python3 examples/speaker_control.py --file examples/test.wav
```

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