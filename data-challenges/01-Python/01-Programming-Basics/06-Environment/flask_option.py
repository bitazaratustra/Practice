# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    if os.getenv('FLASK_ENV') == 'development':
        return 'Starting in development mode...'
    if os.getenv('FLASK_ENV') == 'production':
        return 'Starting in production mode...'
    return 'Starting in empty mode...'

if __name__ == "__main__":
    print(start())
