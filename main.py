import argparse
from file_utils import backup_files

def main():
    parser=argparse.ArgumentParser(
        description="This tool will create a backup in the destination folder"
    )
    parser.add_argument(
        "--source",
        type=str ,
        required=True,
        help="Enter the source folder name"  
    )
    parser.add_argument(
        "--destination",
        type=str ,
        required=True,
        help="Enter the destination folder name"  
    )
    parser.add_argument(
        "--filetypes",
        nargs='+', #Used for list to add multiple values
        required=True,
        help="Enter the filetypes list to be backed up"  
    )
    args=parser.parse_args()
    result={}
    result=backup_files(args.source,args.destination,args.filetypes)
    print(f"{result.keys()}, files were backed-up sucessfully")
if __name__ == "__main__":
    main()