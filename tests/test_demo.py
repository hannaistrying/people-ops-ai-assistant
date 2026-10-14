"""Basic no-dependency checks for the synthetic standalone HTML demo."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'examples/daily-brief-demo.html').read_text(encoding='utf-8')


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.scripts = []
        self.stylesheets = []
        self.details = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and a.get('href', '').startswith('#'):
            self.links.append(a['href'][1:])
        if tag == 'script':
            self.scripts.append(a.get('src'))
        if tag == 'link':
            self.stylesheets.append(a.get('href'))
        if tag == 'details':
            self.details += 1


class DemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = PageParser()
        cls.page.feed(HTML)

    def test_all_toc_links_have_targets(self):
        self.assertGreaterEqual(len(self.page.links), 9)
        self.assertEqual(set(self.page.links) - self.page.ids, set())

    def test_no_remote_script_or_css(self):
        self.assertEqual(self.page.scripts, [None])
        self.assertEqual(self.page.stylesheets, [])
        self.assertNotIn('@import', HTML)

    def test_source_details_and_charts_exist(self):
        self.assertGreaterEqual(self.page.details, 1)
        self.assertIn('class="donut area"', HTML)
        self.assertIn('class="donut nature"', HTML)

    def test_synthetic_label_and_counts(self):
        self.assertIn('Synthetic demo', HTML)
        self.assertEqual(HTML.count('class="work-row"'), 8)
        self.assertIn('Operational</span><b>4 · 50%</b>', HTML)
        self.assertIn('Administrative</span><b>3 · 37.5%</b>', HTML)
        self.assertIn('Strategic</span><b>1 · 12.5%</b>', HTML)

    def test_no_real_internal_links(self):
        self.assertNotIn('mail.google.com/mail/', HTML)
        self.assertNotIn('slack.com/archives/', HTML)
        self.assertNotIn('app.notion.com/p/', HTML)


if __name__ == '__main__':
    unittest.main()
