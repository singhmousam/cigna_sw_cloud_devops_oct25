import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Resize images in a folder and save them to a new location."
    )

    parser.add_argument(
        "--input-dir",
        type=str,
        required=True,
        help="Path to the folder containing input images."
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        required=True,
        help="Destination folder for resized images."
    )

    parser.add_argument(
        "--width",
        type=int,
        default=800,
        help="Target width for resized images (default: 800 pixels)."
    )

    parser.add_argument(
        "--height",
        type=int,
        default=600,
        help="Target height for resized images (default: 600 pixels)."
    )

    parser.add_argument(
        "--keep-aspect",
        action="store_true",
        help="Preserve original aspect ratio during resizing."
    )

    args = parser.parse_args()
    # Your logic here

if __name__ == "__main__":
    main()