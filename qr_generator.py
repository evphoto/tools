#!/usr/bin/env python3
import typer
import qr_code


def main(
    tba: str = typer.Argument('Welcome' , help="tba value for single print"),
    mode: str = typer.Argument('S' , help="application mode")):
    if mode in ('S', 's'):
        print(tba)
        qr_code.generate_code(tba)
        typer.Exit
    else:
        sentinel = ''
        if mode in ('C', 'c'):
            while sentinel not in ('Q', 'q'):
                sentinel = input('Please enter TBA: <Q> to quit: ')
                print(tba)
                qr_code.generate_code(sentinel)
            typer.Exit

if __name__ == '__main__':
    typer.run(main)