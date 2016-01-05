import unittest

from pybabel_htmlbars import extractor


class TestExtraction(unittest.TestCase):
    def test_extraction(self):
        expected_output = [
            (2, 'gettext', ('Singular Mustache statement',), []),
            (4, 'gettext', ('Singular Mustache statement with a %(param)',), []),
            (6, 'ngettext', ('Plural Mustache statement', 'Plural Mustache statements'), []),
            (8, 'gettext', ('Singular sub-expression',), []),
            (10, 'ngettext', ('Plural sub-expression', 'Plural sub-expressions'), []),
            (12, 'gettext', ('Sub-expression with a %(param)',), []),
            (14, 'pgettext', ('Context', 'Message with a context'), []),
            (16, 'pgettext', ('Context', 'Sub-expression with a context'), []),
            (21, 'gettext', ('Deeply nested',), []),
            (26, 'gettext', ('HTML element attribute',), []),
            (29, 'gettext', ('Enclosed by block statement',), []),
            (28, 'gettext', ('Pair in block statement',), []),
            (32, 'gettext', ('Pair in Mustache statement',), []),
            (35, 'gettext', ('Inside a block',), []),
            (37, 'gettext', ('Inside an inverse block',), []),
        ]

        with open('pybabel_htmlbars/test/data/template.hbs') as f:
            output = list(extractor.extract_htmlbars(f))

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
