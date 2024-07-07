""""V(vega) Shell Main File."""

import argparse
import sys

from utils.database import config

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
    user = args['user']
    db_config = config.load_config()
    db_connection = config.connect(db_config)
    iter = 0
    while True:
        if not iter:
            print(f'Welcome to VSH, {user}')
        cmd = input('> ')
        if cmd == 'exit':
            sys.exit(0)
        elif cmd == 'help':
            print_help_msg()
        else:
            print(f'Command is: {cmd}')
        iter += 1

if __name__=='__main__':
    main()