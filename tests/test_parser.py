import unittest
import os
import parser
from datetime import datetime
from pymonad.Either import *


class TestParser(unittest.TestCase):

    def setUp(self):
        self.test_file = datetime.now().strftime('%Y%m%d%H%M%S%f')
        open(self.test_file, 'w+')

    def tearDown(self):
        os.remove(self.test_file)

    def testNoFile(self):
        # no file
        result = parser.parse_file(None)
        assert isinstance(result, Error)

    def testEmptyFile(self):
        # empty file
        result = parser.parse_file(self.test_file)
        assert result.getValue() == []

    def testNonVCard(self):
        # non-vcard file
        with open(self.test_file, 'w+') as test_file:
            test_file.write('bobloblaw')
        result = parser.parse_file(self.test_file)
        assert isinstance(result, Error)
        # single contact, one bad field
        # single contact, one good field
        # single contact, one good field, whitespace before and after
        # single contact, multiple bad fields
        # single contact, multiple good fields
        # multiple contacts
        # multiple contacts, whitespace between

    def testOutputter(self):
        pass
        # No field supplied
        # Bad field supplied
        # No query supplied
        # Bad query supplied
        # Non-matching query supplied
        # Matching query supplied

if __name__ == "__main__":
    unittest.main()
