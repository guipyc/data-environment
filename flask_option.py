# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""

    return f'Starting in {os.getenv("FLASK_ENV", default="empty")} mode...'





if __name__ == "__main__":
    print(start())
