#!/usr/bin/env python3
"""
Copy images to PreTeXt assets directory.
This script prepares images for the PreTeXt build process by copying the
docs/Images/ directory tree into pretext/assets/Images/, which matches the
image source paths used in the PTX source files (e.g. Images/graphing/foo.jpg)
and the external directory configured in publication.ptx (../assets).
"""

import shutil
from pathlib import Path

def main():
    # Define paths
    script_dir = Path(__file__).parent
    source_images_dir = script_dir / "docs" / "Images"
    # pretext/assets/ is the external directory configured in publication.ptx
    # PTX source files reference images as source="Images/<subdir>/<file>"
    pretext_assets_images = script_dir / "pretext" / "assets" / "Images"

    print("Preparing images for PreTeXt book...")
    print(f"Source: {source_images_dir}")
    print(f"Target: {pretext_assets_images}")

    if not source_images_dir.exists():
        print(f"Error: Source images directory not found: {source_images_dir}")
        return 1

    # Copy the entire Images directory tree into pretext/assets/Images/
    if pretext_assets_images.exists():
        shutil.rmtree(pretext_assets_images)
    shutil.copytree(source_images_dir, pretext_assets_images)

    # Count copied files
    total_images = sum(1 for _ in pretext_assets_images.rglob("*") if _.is_file())
    print(f"\nComplete!")
    print(f"  Total images copied to assets/Images: {total_images}")

    return 0

if __name__ == "__main__":
    exit(main())
