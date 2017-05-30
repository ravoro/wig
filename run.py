"""
Sample script for using `wig` to download images from a HTML web page.

Usage:
python run.py http://example.com/page-with-images
"""

import sys

from wig.scrapers import BasicScraper


def get_url_from_arg_or_input():
    """Return url provided as an argument or prompt user to provide the url."""
    for arg in sys.argv:
        if arg.startswith('http'):
            return arg
    return input('url: ')


if __name__ == "__main__":
    url = get_url_from_arg_or_input()
    BasicScraper().run(url)
