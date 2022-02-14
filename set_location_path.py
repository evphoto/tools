#!/usr/bin/env python3
import pathlib
from pathlib import Path

def print_dir_file_list(dir_path):
    #TODO - build regex file name base on file name format
    for i in dir_path.rglob('*.exe'):
        print(i)


def set_path():
    home_directory = Path.home()
    data_folder = 'Downloads'
    data_path = Path(home_directory, data_folder)
    return data_path

def main():
    work_directory = set_path()
    print_dir_file_list(Path(work_directory))


if __name__ == '__main__':
    main()