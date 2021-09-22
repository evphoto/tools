#!/usr/bin/env python3
import csv
import typer

def read_csv(file_name: str):
    print(f'FILE NAME {file_name}')
    """ Opens a csv file and returns a list with the
        contents of the first column (in reality returns a
        list of all the rows contained in the file)

        Args:
            file_name (str): file name and location

        Returns:
            csv_content (list): list with the contents of the
            first column
    """
    try:
        csv_content = []
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                csv_content.append(row[0])
        return csv_content
    except:
        print('Unexpected error')

def main(file_name: str = typer.Argument(...)):
    """ Program receives the name of a csv file and parses the data and
        returns a list of its contents

        Args:
            file_name (str): file name and location

        Returns:
            csv_content (list): csv file content stored in a list
    """
    print(read_csv(file_name))


if __name__ == '__main__':
    typer.run(main)