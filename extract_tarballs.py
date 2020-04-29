"""
Author: Hasan Ali
Date created: 29 April 2020
Tested on: Python v3.8.2 

Purpose: This is a little tool to unpack a folder full of tarballs. The reason I created this instead of using the `tar` tool available on almost every platform, was because I wanted to extract all of the tarballs in the directory at once, and I was not sure how to do that without scripting it. And to ensure cross platform compatibility, I wrote this in Python instead of bash.

Usage:
    `python extract_tarballs.py --help` for usage details.
"""

from os import listdir
from os.path import isfile, join, abspath
import tarfile
import argparse
import sys

def extract_file_to(file, to):
    """
    This function just packages the tarfile calls with some debug print statements.
    """
    print("Extracting [" + file + "] to [" + to + "]...")
    tf = tarfile.open(file, mode="r:gz")
    tf.extractall(path=to)
    tf.close()
    print("Extraction complete.")

def get_list_of_tar_files(path):
    """
    This function takes a path and returns a list of the absolute paths of .tar.gz files in that path.
    """
    try:
        only_files = [f for f in listdir(path) if isfile(join(path, f))]

        tar_files = list(filter(lambda filename: ".tar.gz" in filename, only_files))

        tar_files = list(map(lambda filename: join(path, filename), tar_files))

        return tar_files
    except FileNotFoundError:
        sys.exit("ERROR: [" + path + "] was not found.")

# Parsing command line arguments
parser = argparse.ArgumentParser()

parser.add_argument("location", help="Path to the location containing all the tarballs to be unpacked.")

parser.add_argument("destination", help="Path to the location to extract all the unpacked tarballs.")

args = parser.parse_args()

path = abspath(args.location)
dest = abspath(args.destination)

print("Tarballs location: " + path)
print("Extraction destination: " + dest)

# Tar file processing and extraction.

tar_files = get_list_of_tar_files(path)

# Debug information
for filename in tar_files:
    print("File [" + filename + "] found.")

# Extraction

print("Tarball extraction starting...")

for file in tar_files:
    extract_file_to(file, dest)

print("Tarball extraction complete.")