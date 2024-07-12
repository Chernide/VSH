""""V(vega) Shell Main File."""

import argparse
import os
import pathlib
import sys

from utils.database import database_utils

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

def print_help_msg():
    """Prints the help message for VSH."""
    print(f'{"*" * 15} V(vega)SH {"*" * 15}')
    print('A simple shell written in Python (named after my pup).')
    print('*' * 40)

def main():
    """Main Loop Execution"""
    args = parse_args(sys.argv[1:])
    username = args['user']
    db_config = database_utils.load_config()
    db_connection = database_utils.connect(db_config)
    iter = 0
    pwd = pathlib.Path(os.getcwd())
    while True:
        if iter == 0:
            valid, row = database_utils.check_user(db_connection, username)
            if valid:
                print(f'Welcome back to VSH, {username}. Reseting your pwd...')
                pwd = pathlib.Path(row[1])
                os.chdir(pwd)
                print(os.listdir(pwd))
        cmd = input(f'{pwd}> ')
        if cmd == 'exit':
            sys.exit(0)
        elif cmd == 'help':
            print_help_msg()
        else:
            print(f'Command is: {cmd}')
        iter += 1

if __name__=='__main__':
    main()