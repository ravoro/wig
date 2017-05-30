from unittest import TestCase

from bs4 import BeautifulSoup
from wig.config import BEAUTIFULSOUP_PARSER
from wig.scrapers import BasicScraper


class Test(TestCase):
    def setUp(self):
        self.scraper = BasicScraper()
        self.mock_html = BeautifulSoup(
            """
            <html><body><div>
            <p>randomcontent</p>
            <p>randomtext</p>
            </div></body></html>
            """, BEAUTIFULSOUP_PARSER)

    def test_raise_exception_when_no_match(self):
        """Raise an exception when the selector is not able to match."""
        with self.assertRaises(Exception):
            self.scraper.html_main_container(self.mock_html, 'randomtag')

    def test_raise_exception_when_multiple_matches(self):
        """Raise an exception when the selector is able to match more than one item."""
        with self.assertRaises(Exception):
            self.scraper.html_main_container(self.mock_html, 'p')

    def test_return_subset_html(self):
        """Return subset of the provided html, as specified by the selector."""
        expect = self.mock_html.select_one('div')
        result = self.scraper.html_main_container(self.mock_html, 'div')
        assert result == expect

    def test_return_subset_html_default(self):
        """Return 'body' tag, when no explicit selector is specified."""
        expect = self.mock_html.select_one('body')
        result = self.scraper.html_main_container(self.mock_html)
        assert result == expect
