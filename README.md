# best-practices
## Purpose
This repository contains a python file that contains 2 functions that calculate the mean and standard deviation of a vector of integers
The vector of integers must be supplied by a column from a *tab separated file*, where the column number and file name are the 2 inputs to the python main function

## Usage
The file "get_column_stats.py" can be used as a library that contains a
- calculate_mean(vec) is a function that takes a list/vector of ints; vec; and returns its arithmetic mean
- calculate_stdev(vec) is a function that takes a list/vector of ints; vec; and returens its standard deviation
It can also be used as an executable using argparse to take in a file name and column number
- parameters
 - --input_filename    <--- file name to be read in
 - --column_number     <--- number of column of which the mean and stdev is calculated and printed

Example:
Type this into your terminal:
python3 get_column_stats.py --input_filename data.txt --column_number 7

The mean and standard deviation of the integers in column seven in data.txt should be printed.

## Minimum Requirements to run

- Python 3.7.4