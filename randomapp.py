import argparse

from utils import read_filtered_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Filter a directory for the specified file type and generate a file level dict"
    )

    parser.add_argument(
        "dir_path",
        type=str,
        help="Source path for file ops"
    )

    parser.add_argument(
        "allowed_file_type",
        type=list,
        help="Allowed file types to read frpm source directpry",
        default=['txt']
    )

    args = parser.parse_args()
    print('Dir Path', args.dir_path)

    print(f'Initialing file ops ')
    filtered_content = read_filtered_files(args.dir_path, args.allowed_file_type)
    print()
