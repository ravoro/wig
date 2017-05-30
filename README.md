# WIG _"the Web Image Getter"_

Framework for locating and downloading images from HTML web pages.

## How it works
`wig` provides you with a basic default HTML images scraper (`wig.scrapers.BasicScraper`).

The scraper's `run` method takes a URL as an argument and does the following:
- Fetch the URL's HTML
- Locate the parent HTML element containing images _(default: `<body>` tag)_
- Within the container element, locate the HTML elements containing individual images _(default: `<img>` tags)_
- Determine the URLs for each image resource (default: `src` attribute of each `<img>` tag)
- Download each image resource (default destination: `~/Downloads/wig`)

## Examples
`run.py` is a basic script that uses `wig` to download images from any web site.

## Tests
- Run tests: `./scripts/test.sh`
- Run coverage: `./scripts/test_coverage.sh`