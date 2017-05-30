from unittest import TestCase

from bs4 import BeautifulSoup
from wig.config import BEAUTIFULSOUP_PARSER
from wig.scrapers import BasicScraper


class Test(TestCase):
    def setUp(self):
        self.scraper = BasicScraper()
        self.author = 'randomauthor'
        self.mock_html = BeautifulSoup(
            """
            <html><body>
            <div>{}</div>
            <p>randomtext</p>
            </body></html>
            """.format(self.author), BEAUTIFULSOUP_PARSER)

    def test_return_page_author(self):
        """Return the page author value, as specified by the selector."""
        result = self.scraper.get_page_meta_author(self.mock_html, 'div')
        assert result == self.author

    def test_raise_exception_when_no_match(self):
        """Raise an exception when the selector is not able to match."""
        with self.assertRaises(Exception):
            self.scraper.get_page_meta_author(self.mock_html, 'randomtag')

    def test_return_page_author_stripped(self):
        """Return the page author value stripped of any surrounding whitespaces."""
        author_spaces = ' {}  '.format(self.author)
        self.mock_html.find(text=self.author).string.replace_with(author_spaces)  # add spaces to html
        result = self.scraper.get_page_meta_author(self.mock_html, 'div')
        assert result == self.author
        assert result != author_spaces
