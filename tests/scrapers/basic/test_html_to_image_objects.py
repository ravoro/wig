from unittest import TestCase

from bs4 import BeautifulSoup
from wig.config import BEAUTIFULSOUP_PARSER
from wig.scrapers import BasicScraper


class Test(TestCase):
    def setUp(self):
        self.scraper = BasicScraper()
        self.mock_html = BeautifulSoup(
            """
            <img src='http://example.com/a.jpg' />
            <img src='http://example.com/b.jpg' />
            <ul>
            <li>http://example.com/123.png</li>
            <li>http://example.com/789.png</li>
            </ul>
            """, BEAUTIFULSOUP_PARSER)
        self.mock_url = 'http://example.com'
        self.mock_containers = self.mock_html.select('img')

    def test_raise_exception_when_no_match(self):
        """Raise an exception when the selector is not able to match."""
        with self.assertRaises(Exception):
            self.scraper.html_to_image_objects(self.mock_containers, self.mock_url, lambda tag: tag['srcc'])

    def test_return_image_objects(self):
        """Return image objects for images matched by the selector."""
        self.mock_containers = self.mock_html.select('li')
        result = self.scraper.html_to_image_objects(self.mock_containers, self.mock_url, lambda tag: tag.string)
        assert result == ["http://example.com/123.png", "http://example.com/789.png"]

    def test_return_image_objects_default(self):
        """Return image objects using the img[src] matcher, when no explicit selector is specified."""
        result = self.scraper.html_to_image_objects(self.mock_containers, self.mock_url)
        assert result == ["http://example.com/a.jpg", "http://example.com/b.jpg"]

    def test_return_absolute_urls(self):
        """Return all found urls as absolute urls."""
        self.mock_html = BeautifulSoup(
            """
            <img src='aaa.jpg' />
            <img src='bbb.jpg' />
            """, BEAUTIFULSOUP_PARSER)
        self.mock_containers = self.mock_html.select('img')
        result = self.scraper.html_to_image_objects(self.mock_containers, self.mock_url)
        assert result == ["http://example.com/aaa.jpg", "http://example.com/bbb.jpg"]
