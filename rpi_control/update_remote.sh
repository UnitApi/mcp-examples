#!/bin/bash
# update_remote.sh: Sync all files in rpi_control to a remote Raspberry Pi
# Usage: bash update_remote.sh user@remote_host [remote_path] or set REMOTE in .env
set -e

# Load .env if present
if [ -f .env ]; then
  set -a
  . ./.env
  set +a
fi

REMOTE="${1:-$REMOTE}"
REMOTE_PATH="${2:-$REMOTE_PATH}"

# If REMOTE or REMOTE_PATH are still empty, set sensible defaults
if [ -z "$REMOTE" ]; then
    REMOTE=$(grep '^REMOTE=' .env | cut -d'=' -f2 | tr -d '"')
fi
if [ -z "$REMOTE_PATH" ]; then
    REMOTE_PATH=$(grep '^REMOTE_PATH=' .env | cut -d'=' -f2 | tr -d '"')
fi
if [ -z "$REMOTE_PATH" ]; then
    REMOTE_PATH=~/rpi_control
fi

if [ -z "$REMOTE" ]; then
    echo "Usage: $0 user@remote_host [remote_path] or set REMOTE in .env"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Ensure remote path exists (same logic as install_remote.sh)
ssh "$REMOTE" "mkdir -p $REMOTE_PATH"

# Sync all files except venv, .git, __pycache__, and large audio files
rsync -avz --exclude 'venv' --exclude '.git' --exclude '__pycache__' "$SCRIPT_DIR/" "$REMOTE":"$REMOTE_PATH"/

echo "[update_remote.sh] Files synced to $REMOTE:$REMOTE_PATH"
