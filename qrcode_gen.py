#!/usr/bin/env python3
import qrcode
from qrcode import constants
import typer
import csv

def generate_code(img_name: str):
    """ Generated a .png QR code with the contents of
        img_name data as its content

    Args:
        img_name (str): string data to be encoded


    Returns:
        .png: QR code in .png format 
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # remove new line attached by cal program
    # TODO: test with Excel to see if it does the same
    frmt_name = img_name.replace("\n", "")

    qr.add_data(frmt_name)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white")
    img.save(frmt_name + '.png')


def parse_csv(csv_file: str):
    """ Opens and parse a csv file

    Args:
        csv_file (str): file name object

    Returns:
        null:
    """
    with open(csv_file) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in file:
            generate_code(img_name = row)


def main(csv_file: str = typer.Argument(...)):
    """ Program parses a csv file and generates a QR code
        of each element placed in the first column. 

        Do not add headers, copy the raw data into the first
        column with no formatting.

    Args:
        file_loc (str): Location of the spreadsheet
    

    Returns:
        null: generates a .png file of each element 
    """
    parse_csv(csv_file)


if __name__ == '__main__':
    typer.run(main)