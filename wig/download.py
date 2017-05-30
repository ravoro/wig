"""Helper module for downloading web resources."""

import logging
import time
import urllib.request

import os
from bs4 import BeautifulSoup

from .config import DOWNLOAD_USER_AGENT, DOWNLOAD_DELAY_SECONDS, BEAUTIFULSOUP_PARSER


def download_html(url):
    """Return a BeautifulSoup representation of html at the given url."""
    logging.debug("Getting html from: {}".format(url))
    request_with_user_agent = urllib.request.Request(url, headers={'User-Agent': DOWNLOAD_USER_AGENT})
    page_bytes = urllib.request.urlopen(request_with_user_agent).read()
    page_html = page_bytes.decode('utf-8', 'replace')
    return BeautifulSoup(page_html, BEAUTIFULSOUP_PARSER)


def download_files(files, dst_dir):
    """Download a list of files, with a delay between downloads."""
    for f in files:
        time.sleep(DOWNLOAD_DELAY_SECONDS)
        download_file(f, dst_dir)


def download_file(url, dst_dir):
    """Download the file identified by `url` and save it in `dst_dir` directory."""
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    dst_file_path = _url_to_file_path(url, dst_dir)

    logging.info('Downloading "{}" to "{}"'.format(url, dst_file_path))
    urllib.request.urlretrieve(url, dst_file_path)


def _url_to_file_path(url, dst_dir):
    """Return file path where the resource at `url` should be stored after download."""
    filename = os.path.basename(url)
    dst_file_path = os.path.join(dst_dir, filename)

    # if the file already exists, prompt the user to provide a new file name or confirm an overwrite of the file
    while os.path.exists(dst_file_path):
        user_overwrite_str = 'Attempting to download "{0}" to "{1}", but the file already exists.\n' \
                             'Overwrite "{1}"? [yes/NO] '.format(url, dst_file_path)
        user_overwrite = input(user_overwrite_str).strip().lower()
        if user_overwrite and user_overwrite[0] == 'y':
            break
        user_new_filename_str = 'New name for "{}": '.format(os.path.basename(dst_file_path))
        user_new_filename = input(user_new_filename_str).strip()
        if user_new_filename:
            dst_file_path = os.path.join(dst_dir, user_new_filename)

    return dst_file_path
