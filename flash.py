#!/usr/bin/env python3
"""Download latest zmk-config GitHub Actions artifacts and flash to nice!nano."""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

FIRMWARE_DIR = Path("firmware")
NICENANO = Path("/Volumes/NICENANO")

FIRMWARE_FILES = {
    "left":  "custom_split_left-nice_nano_v2-zmk.uf2",
    "right": "custom_split_right-nice_nano_v2-zmk.uf2",
    "reset": "settings_reset-nice_nano_v2-zmk.uf2",
}


def get_latest_run_id() -> str:
    result = subprocess.run(
        ["gh", "run", "list", "--json", "databaseId", "--jq", ".[].databaseId"],
        capture_output=True, text=True, check=True,
    )
    ids = [line for line in result.stdout.splitlines() if line.strip()]
    if not ids:
        sys.exit("No runs found.")
    return ids[0]


def download_run(run_id: str) -> None:
    if FIRMWARE_DIR.exists():
        print(f"Removing existing {FIRMWARE_DIR}/")
        shutil.rmtree(FIRMWARE_DIR)
    subprocess.run(["gh", "run", "download", run_id], check=True)


def copy_firmware(side: str) -> None:
    src = FIRMWARE_DIR / FIRMWARE_FILES[side]
    if not src.exists():
        sys.exit(f"Firmware not found: {src}")
    if not NICENANO.exists():
        sys.exit(f"NICENANO volume not mounted at {NICENANO}. "
                 f"Double-tap reset on the controller and try again.")
    dest = NICENANO / src.name
    print(f"Copying {src} -> {dest}")
    shutil.copy(src, dest)
    print("Done.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--reset", action="store_true", help="flash settings reset firmware")
    group.add_argument("--left",  action="store_true", help="flash left half firmware")
    group.add_argument("--right", action="store_true", help="flash right half firmware")
    args = parser.parse_args()

    side = "reset" if args.reset else "left" if args.left else "right"

    run_id = get_latest_run_id()
    print(f"Latest run: {run_id}")
    download_run(run_id)
    copy_firmware(side)


if __name__ == "__main__":
    main()
