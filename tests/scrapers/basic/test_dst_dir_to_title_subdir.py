from unittest import TestCase

from wig.scrapers import BasicScraper


class Test(TestCase):
    def setUp(self):
        self.scraper = BasicScraper()
        self.mock_dst_dir = "/home/user/wig-downloads/"
        self.mock_page_meta = {'title': 'Random title'}

    def test_return_dst_dir_with_title_subdir(self):
        """Return the dst_dir with a subdir that uses the page's title."""
        result = self.scraper.dst_dir_to_title_subdir(self.mock_dst_dir, self.mock_page_meta)
        assert result == "/home/user/wig-downloads/Random title"
