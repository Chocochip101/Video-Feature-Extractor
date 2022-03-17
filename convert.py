from fileinput import filename
import h5py
import numpy as np
import argparse
import os
parser = argparse.ArgumentParser(description='Numpy to h5 converter')

    
parser.add_argument('--numpy_dir', type=str, default="/NumpyResult",
                            help='Numpy file dirctory')

parser.add_argument('--output_dir', type=str, default='/h5Result',
                            help='Output directory')

parser.add_argument('--ouput_filename', type=str, default='result',
                            help='File Name of h5 file')

args = parser.parse_args()


NP_PATH = args.numpy_dir
OUTPUT_PATH = args.output_dir
OUTPUT_FILENAME = args.ouput_filename
file_list = os.listdir('./' + NP_PATH)

if len(file_list) == 0:
    "No Numpy File Found!"
else:
    for file_name in file_list:
        try:
            weights = np.load(NP_PATH + os.sep + file_name)
            with h5py.File(OUTPUT_FILENAME + '.h5', 'w') as hf:
                hf.create_dataset(file_name[:len(file_name) - 3], data=weights)
        except:
            print("Error: loading numpy file ~", file_name)
            continue
        