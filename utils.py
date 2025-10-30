import os

def read_filtered_files(path, file_type=['txt']):
    """
    Create a dict of read files on basis of applied filters

    Pramaeters:
    path (str): Path of input dir to read
    file_type (list) Optional: Inclusive list of file ext to read 

    Returns:
    file_dict (dict): File conetnt for each file name
    """
    print('Caller Name: ' + __name__)
    file_dict = {}
    for f in [file for file in os.listdir(path) if file.split('.')[-1] in file_type]:
        correct_path = os.path.join(path, f)
        try:
            with open(correct_path, 'r') as fo:
                file_dict[f] = fo.read()
        except Exception as e:
            file_dict[f] = "!! WARNING !! File read operation failed with " + str(e)
    return file_dict


if __name__ == '__main__':
    print('This is utility class scpript')