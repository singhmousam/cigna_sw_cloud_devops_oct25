from utils import *

import sys

arg0 = sys.argv[0]
input_path = sys.argv[1]
filtered_file_type = sys.argv[2]
# arg3 =sys.argv[3]

print('Called by: ', __name__)
# {", ".join(filtered_file_type)} 
print(f'Initialing file ops for filtering {filtered_file_type} from dir {input_path}')
filtered_content = read_filtered_files(input_path, filtered_file_type)
print()

with open('output.txt', 'w') as fo:
    fo.write(str(filtered_content))

print('Output file generated successfully')

# python app.py "c://Download" ["txt", "csv"]