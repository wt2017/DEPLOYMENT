#!/bin/bash

set -e

error_exit() {
  echo $*
  exit 1
}

echo "== Running ComfyUI"

cd mnt
source venv/bin/activate

cd ComfyUI
# Full list of CLI options at https://github.com/comfyanonymous/ComfyUI/blob/master/comfy/cli_args.py
python3 ./main.py --listen 0.0.0.0 --disable-auto-launch
