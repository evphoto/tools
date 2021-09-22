#!/usr/bin/env python3
import qrcode
import typer
import io

def generate_code(img_name: str):
    qr = qrcode.QRCode()
    qr.add_data(img_name)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())


def main(data: str = typer.Argument(...)):
    for i in range(2):
        generate_code(data)


if __name__ == '__main__':
    typer.run(main)