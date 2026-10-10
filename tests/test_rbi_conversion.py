import importlib.util
import unittest
from tools.rbi_html_to_markdown import convert


@unittest.skipUnless(importlib.util.find_spec('lxml'), 'Optional RBI acquisition helper requires lxml')
class RBIConversionTests(unittest.TestCase):
    def page(self, body):
        return ('<html><nav>IGNORE MENU</nav><table><tr><td class="tableheader"><b>Test direction</b></td></tr>'
                '<tr class="tablecontent2"><td>'+body+'</td></tr></table><footer>IGNORE FOOTER</footer></html>').encode()

    def test_article_only_and_source_link(self):
        title,text,qa=convert(self.page('<p class="head">Scope</p><p>Only banks <a href="/source">details</a>.</p>'),'https://www.rbi.org.in/Scripts/test')
        self.assertNotIn('IGNORE',text)
        self.assertIn('## Scope',text)
        self.assertIn('(https://www.rbi.org.in/source)',text)
        self.assertTrue(qa['retained_source_token_sequence'])
        self.assertFalse(qa['pdf_pagination_verified'])

    def test_table_cells_and_footnote_retained(self):
        _,text,qa=convert(self.page('<table><tr><td>Category</td><td>Amount</td></tr><tr><td>A</td><td>₹15,000<sup>1</sup></td></tr></table><p>1 Exception.</p>'),'https://www.rbi.org.in/')
        self.assertIn('| A | ₹15,000 [1] |',text)
        self.assertIn('1 Exception.',text)
        self.assertEqual(qa['tables'],1)

    def test_ambiguous_body_rejected(self):
        with self.assertRaisesRegex(ValueError,'exactly one'):
            convert(b'<table><tr class="tablecontent2"></tr><tr class="tablecontent2"></tr></table>','https://www.rbi.org.in/')

    def test_embedded_image_requires_review(self):
        with self.assertRaisesRegex(ValueError,'image'):
            convert(self.page('<p>A requirement <img src="table.png"></p>'),'https://www.rbi.org.in/')


if __name__=='__main__':unittest.main()
