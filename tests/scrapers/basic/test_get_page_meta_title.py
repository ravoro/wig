from unittest import TestCase

from bs4 import BeautifulSoup
from wig.config import BEAUTIFULSOUP_PARSER
from wig.scrapers import BasicScraper


class Test(TestCase):
    def setUp(self):
        self.scraper = BasicScraper()
        self.title = 'randomtitle'
        self.mock_html = BeautifulSoup(
            """
            <html>
            <head><title>{}</title></head>
            <body><h1>anothertitle</h1></body>
            </html>
            """.format(self.title), BEAUTIFULSOUP_PARSER)

    def test_raise_exception_when_no_match(self):
        """Raise an exception when the selector is not able to match."""
        with self.assertRaises(Exception):
            self.scraper.get_page_meta_title(self.mock_html, 'randomtag')

    def test_return_page_title(self):
        """Return the page title value, as specified by the selector."""
        result = self.scraper.get_page_meta_title(self.mock_html, 'h1')
        assert result == 'anothertitle'
        assert result != self.title

    def test_return_page_title_default(self):
        """Return the page title value equal to the 'title' tag value, when no selector specified. """
        result = self.scraper.get_page_meta_title(self.mock_html)
        assert result == self.title
        assert result != 'anothertitle'

    def test_return_page_title_stripped(self):
        """Return the page title value stripped of any surrounding whitespaces."""
        title_spaces = ' {}  '.format(self.title)
        self.mock_html.find(text=self.title).string.replace_with(title_spaces)  # add spaces to html
        result = self.scraper.get_page_meta_title(self.mock_html)
        assert result == self.title
        assert result != title_spaces
