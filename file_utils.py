import os
import shutil

def backup_files(source, destination, filetypes):
    """
    This function copies the specific extension files (Backup) from one source to the destination
    into their respective folder based on its extension.
    
    Parameter:
    source (str): Source Directory Path
    destination (str): Destination Directory Path
    filetypes (list): List of file extension to be backed up
    
    Return:
    dict: Dictionary containing filenames and their content
    """
    content = {}

    if not os.path.exists(source):
        print("Source does not exist")
        raise FileNotFoundError(f"{source} Does Not Exist")

    try:
        if os.path.exists(destination):
            for i in filetypes:
                try:
                    os.mkdir(os.path.join(destination, i))
                except FileExistsError:
                    pass
                except Exception as e:
                    print(f"Error creating subfolder {i}: {e}")

            for fname in [file for file in os.listdir(source) if file.split('.')[-1] in filetypes]:
                try:
                    with open(os.path.join(source, fname), 'r') as f:
                        content[fname] = f.read()
                    shutil.copy(
                        os.path.join(source, fname),
                        os.path.join(destination, fname.split('.')[-1], fname)
                    )
                except Exception as e:
                    print(f"Error processing file {fname}: {e}")
        else:
            try:
                os.mkdir(destination)
            except Exception as e:
                print(f"Error creating destination folder: {e}")
                raise

            for i in filetypes:
                try:
                    os.mkdir(os.path.join(destination, i))
                except FileExistsError:
                    pass
                except Exception as e:
                    print(f"Error creating subfolder {i}: {e}")

            for fname in [file for file in os.listdir(source) if file.split('.')[-1] in filetypes]:
                try:
                    with open(os.path.join(source, fname), 'r') as f:
                        content[fname] = f.read()
                    shutil.copy(
                        os.path.join(source, fname),
                        os.path.join(destination, fname.split('.')[-1], fname)
                    )
                except Exception as e:
                    print(f"Error processing file {fname}: {e}")
    except Exception as e:
        print(f"Unexpected error during backup: {e}")
        raise

    return content