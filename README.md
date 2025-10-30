________________________________________
## Problem Statement: "Backup Organizer CLI Tool"
### Objective
Create a Python script that organizes and backs up files from a source directory into a destination directory based on file types. The script should be modular, accept command-line arguments, handle exceptions gracefully, and use basic data structures for organization.
________________________________________
### Functional Requirements
1.	Command-Line Arguments (argparse)
Accept the following arguments:
o	--source: Path to the source directory
o	--destination: Path to the destination directory
o	--filetypes: Comma-separated list of file extensions to include (e.g., .txt,.jpg)
2.	Directory and File Operations (os, shutil)
o	Validate that the source directory exists.
o	Create destination subfolders based on file extensions.
o	Copy matching files into their respective subfolders.
3.	Modular Design
o	Split the logic into at least two modules: 
	file_utils.py: Functions for scanning, filtering, and copying files.
	main.py: CLI entry point that uses argparse and calls file_utils.
4.	Exception Handling
o	Handle missing directories, permission errors, and invalid file types.
o	Print user-friendly error messages.
5.	Data Structures
o	Use dictionaries to group files by extension.
o	Use lists to store file paths.

________________________________________
### Example Usage
python main.py --source ./downloads --destination ./backup --filetypes .pdf,.png
This should:
•	Scan ./downloads for .pdf and .png files
•	Create ./backup/pdf/ and ./backup/png/
•	Copy files accordingly
