from unittest import TestCase

from bs4 import BeautifulSoup
from wig.config import BEAUTIFULSOUP_PARSER
from wig.scrapers import BasicScraper


class Test(TestCase):
    def setUp(self):
        self.scraper = BasicScraper()
        self.mock_html = BeautifulSoup(
            """
            <main>
            <div><img src="a.jpg"/></div>
            <div><img src="b.jpg"/></div>
            <div><p>hello</p></div>
            </main>
            """, BEAUTIFULSOUP_PARSER)

    def test_raise_exception_when_no_match(self):
        """Raise an exception when the selector is not able to match."""
        with self.assertRaises(Exception):
            self.scraper.html_image_containers(self.mock_html, 'randomtag')

    def test_return_image_containers(self):
        """Return the tags matched by the selector."""
        expect = self.mock_html.select('div')
        result = self.scraper.html_image_containers(self.mock_html, 'div')
        assert len(result) == 3
        assert result == expect

    def test_return_image_containers_default(self):
        """Return the 'img' tags, when no explicit selector is specified."""
        expect = self.mock_html.select('img')
        result = self.scraper.html_image_containers(self.mock_html)
        assert len(result) == 2
        assert result == expect
