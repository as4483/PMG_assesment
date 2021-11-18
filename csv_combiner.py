"""CSV Combiner

This script takes several CSV files as input

This tool accepts and validates comma separated value files (.csv)
and appends the file's basename in a column at the end of a row
from each input. filename as the header for the additional column.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * combine_files - returns the result to stdout
    * main - the main function of the script
"""

__author__ = "Amogh Vikram Sirohi"

import argparse
import sys
import os
import pandas as pd


class Combine:

    def __init__(self):
        self.testArgs = []

    def combine_files(self):
        """
        Combines multiple CSV files row wise and appends the filename to a column at the end
        """

        if not self.testArgs:
            my_parser = argparse.ArgumentParser(description='Combine multiple csv files row wise and append the filename '
                                                            'column at the end, results seen on stdout')

            my_parser.add_argument('files', metavar='files', nargs='+', type=argparse.FileType('r'),
                                   help='Give required csv files as input')

            args = my_parser.parse_args()

            self.testArgs = [input_file.name for input_file in args.files]

        # lambda function to validate file type
        def f(x):
            return x.lower().endswith('csv')

        if not all(f(input_file) for input_file in self.testArgs):
            sys.stderr.write('All inputs must be .csv')
        else:
            # list to store a row
            row = []

            for file in self.testArgs:
                # read the csv file as a chunk since file size can be > 2GB
                for chunk in pd.read_csv(file, chunksize=100000):
                    # get files basename
                    file_name = os.path.basename(file)
                    # add the 'filename' column to the chunk
                    chunk['filename'] = file_name
                    row.append(chunk)

            # convert chunk to csv and print it
            for chunk in row:
                print(chunk.to_csv(index=False, header=True, line_terminator='\n', chunksize=100000), end='')


def main():
    lol = Combine()
    lol.combine_files()


if __name__ == '__main__':
    main()
