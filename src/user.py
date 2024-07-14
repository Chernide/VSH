"""Class for the current VSH user."""

import pathlib

class user:
    """VSH user class."""

    def __init__(self, username: str, pwd: pathlib.Path = None) -> None:
        """User class init.
        
        Args:
            username:
                Current username
            pwd:
                Present working directory for that user.
        
        """
        self.username = username
        self.pwd = pwd
        self.prev_cmds = []
        
    def add_cmd(self, cmd: str) -> None:
        """Adds command to prev_cmds list.
        
        Args:
            cmd:
                Command issued.
        
        """
        self.prev_cmds.append(cmd)