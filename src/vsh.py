"""Driver for the VSH shell."""

import glob
import os
import pathlib
import sys

from colorama import Fore, Style

from utils.database import database_utils

import user

class vsh:
    """VSH driver."""

    def __init__(self, user: user.user) -> None:
        self.cur_user = user
        self.pwd = None

        self.cmds = {
            'ls': self.list_dir,
        }

    def print_help_msg(self) -> None:
        """Prints the help message for VSH."""
        print(f'{"*" * 15} V(vega)SH {"*" * 15}')
        print('A simple shell written in Python (named after my pup).')
        print('*' * 40)

    def list_dir(self, cmd: str, opts: list[str] = None):
        """Function to list pwd.
        
        Args:
            cmd:
                Inputted command.
            opts:
                Any extra options on the command.
        
        """
        for file_path in glob.glob(f'{self.pwd}/*'):
            filename = file_path.split('/')[-1]
            if os.path.isdir(file_path):
                print(Fore.GREEN + filename + Style.RESET_ALL)
            else:
                print(filename)

    def start_shell(self) -> None:
        """Main while loop for VSH."""
        db_config = database_utils.load_config()
        db_connection = database_utils.connect(db_config)
        iter = 0
        while True:
            if iter == 0:
                valid, row = database_utils.check_user(db_connection, self.cur_user)
                if valid:
                    print(f'Welcome back to VSH, {self.cur_user}. Reseting your pwd...')
                    self.pwd = pathlib.Path(row[1])
                    os.chdir(self.pwd)
                else:
                    print(f'Welcome new user, {self.cur_user}!')
                    self.pwd = os.getcwd()
            cmd = input(f'{self.pwd}> ')
            if cmd == 'exit':
                sys.exit(0)
            elif cmd == 'help':
                self.print_help_msg()
            else:
                cmd_list = cmd.split(' ')
                base_cmd = cmd_list[0]
                cmd_options = ''
                if len(cmd_list) > 1:
                    cmd_options = cmd_list[1:]
                func = self.cmds.get(base_cmd, None)
                if func:
                    func(base_cmd, cmd_options)
                else:
                    print(f'Command {cmd} unknown.')
            iter += 1