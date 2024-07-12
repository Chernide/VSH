"""Utility functions for accessing postgresql database."""

import psycopg2

from configparser import ConfigParser

def check_user(conn, username: str) -> tuple[bool, dict]:
    """Checks if the user is in the database

    Args:
        conn:
            Database connnection.
        username:
            User that is being looked up.
    """
    with conn.cursor() as cur:
        cur.execute(f'SELECT * FROM users where username = \'{username}\'')
        row = cur.fetchone()
        if row is not None:
            return (True, row)
        return (False, row)

def load_config(filename: str = 'database.ini', section: str ='postgresql') -> dict:
    """Read and load the data stored in the ini file.

    Args:
        filename:
            The location of the ini file.
        section:
            Name of the section to load.

    Returns:
        config:
            A dictionary containing the database configuration.

    """
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section, {section}, not found in file, {filename}.')

    return config


def connect(config: dict):
    """Connect to the postgresql database server.
    
    Args:
        config:
            Database configuration
    
    """

    try:
        with psycopg2.connect(**config) as conn:
            print('Successfully connected to PostgreSQL Server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as e:
        print(e)