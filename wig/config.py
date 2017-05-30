"""Default config for wig."""

import logging

import os

# logging level to be used by the `logging` module
LOGGING_LEVEL = logging.ERROR

# base destination dir for saving images
DST_DIR_BASE = os.path.join(os.path.expanduser('~'), 'Downloads', 'wig')

# user agent string to use when making a HTTP request
DOWNLOAD_USER_AGENT = 'WIG/0.1'

# delay to use between downloads (a courtesy delay to avoid putting too much stress on the server)
DOWNLOAD_DELAY_SECONDS = 1

# parser used by beautifulsoup
BEAUTIFULSOUP_PARSER = 'html.parser'
