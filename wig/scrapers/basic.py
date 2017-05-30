"""
A basic HTML image scraper.

Identifies image resources by looking for <img> tags within <body>.
"""

import logging
import os.path
from urllib.parse import urljoin

import os
from wig.config import DST_DIR_BASE


class BasicScraper:
    def run(self, url):
        """Download any images identified by the scraper for the given url."""
        from wig.download import download_html, download_files

        html = download_html(url)
        # logging.debug("Fetched HTML: {}".format(html))

        page_meta = self.get_page_meta_data(html)
        logging.debug("Page meta data: {}".format(page_meta))

        main_html = self.html_main_container(html)
        logging.debug("HTML main container: {}".format(main_html))

        image_containers = self.html_image_containers(main_html)
        logging.debug("HTML image containers (count: {}): {}".format(len(image_containers), image_containers))

        image_objects = self.html_to_image_objects(image_containers, url)
        logging.debug("Image objects (count: {}): {}".format(len(image_objects), image_objects))

        dst_dir = DST_DIR_BASE
        dst_dir_updated = self.dst_dir_to_title_subdir(dst_dir, page_meta)
        os.makedirs(dst_dir_updated, exist_ok=True)

        download_files(image_objects, dst_dir_updated)

    def get_page_meta_data(self, html):
        """Return the page meta data."""
        return {
            'author': self.get_page_meta_author(html),
            'title': self.get_page_meta_title(html)
        }

    def get_page_meta_author(self, html, selector=None):
        """Return the page author."""
        if not selector:
            return None
        result = html.select_one(selector)
        if not result:
            raise Exception('The selector returned no results.')
        return result.string.strip()

    def get_page_meta_title(self, html, selector=None):
        """Return the page title."""
        selector = 'title' if not selector else selector
        result = html.select_one(selector)
        if not result:
            raise Exception('The selector returned no results.')
        return result.string.strip()

    def html_main_container(self, html, selector=None):
        """Return subset of html that is the main container of images that should be considered."""
        selector = 'body' if not selector else selector
        result = html.select(selector)
        if not result:
            raise Exception('The selector returned no results.')
        if len(result) > 1:
            raise Exception('The selector returned multiple results.')
        return result[0]

    def html_image_containers(self, html, selector=None):
        """Return list of html tags, where each tag contains an image url and any relevant image meta data."""
        selector = 'img' if not selector else selector
        result = html.select(selector)
        if not result:
            raise Exception('The selector returned no results.')
        return result

    def html_to_image_objects(self, containers, page_url, selector=None):
        """Convert html tags to image objects, by extracting relevant data."""
        selector = (lambda tag: tag['src']) if not selector else selector

        # find image urls
        found_images = [selector(c) for c in containers]
        logging.debug("Found images (count: {}): {}".format(len(found_images), found_images))

        # ensure absolute urls
        images = [urljoin(page_url, i) for i in found_images]
        logging.debug("Absolute path images (count: {}): {}".format(len(images), images))

        return images

    def dst_dir_to_title_subdir(self, dst_dir, page_meta):
        """Return a path to a sub directory of `dst_dir` with page title as the dir name."""
        return os.path.join(dst_dir, page_meta['title'])
