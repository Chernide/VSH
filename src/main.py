""""V(vega) Shell Main File."""

import argparse
import os
import pathlib
import sys

from utils.database import database_utils

import vsh

def parse_args(args: str) -> dict:
    """Parsing CLI args.

    Args:
        args:
            Inputted CLI args.
    
    Returns: dict
        Dictionary containing parsed CLI args.

    """

    parser = argparse.ArgumentParser(
        prog='V(vega)SH',
        description='A simple shell written in Python (named after my pup).'
    )

    parser.add_argument(
        '-u', '--user',
        required=True,
        type=str,
        help=(
            'The desired users shell.'
        )
    )

    return vars(parser.parse_args(args))

def main():
    """Main Loop Execution"""
    args = parse_args(sys.argv[1:])
    username = args['user']
    VSH = vsh.vsh(username)
    VSH.start_shell()


if __name__=='__main__':
    main()