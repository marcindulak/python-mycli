import argparse

from mycli.prt import prt  # print is a Python statement
from mycli.run import run
from mycli.case import case

def create_parser():
    parser = argparse.ArgumentParser(
        description='A Python program that demonstrates usage of argparse',
    )

    parser.add_argument("--print", dest='prt',
                        action="store_true", help="Print")
    parser.add_argument("--run", action="store_true", help="Run")
    parser.add_argument('--case', choices=[0, 1, 2],  # can be extended ...
                        type=int, action='append', help="Case 0, 1, 2")

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.prt:
        prt()
    if args.run:
        run()
    if args.case:
        case(list(set(args.case)))  # make case arguments unique
