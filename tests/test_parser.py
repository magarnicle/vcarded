import unittest
import parser
from pymonad.Either import *


class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNoFile(self):
        # no file
        result = parser.parse_file(None)
        assert isinstance(result, Error)

    def testNonExistantFile(self):
        """Parsing a non-existant file returns an error."""
        result = parser.parse_file('tests/test_files/an_imaginary_file.txt')
        assert isinstance(result, Error)

    def testEmptyFile(self):
        # empty file
        result = parser.parse_file('tests/test_files/empty.txt')
        assert result.getValue() == []

    def testNonVCard(self):
        # non-vcard file
        result = parser.parse_file('tests/test_files/non_vcard.txt')
        assert isinstance(result, Error)

    def testSingleContactOneBadField(self):
        # single contact, one bad field
        result = parser.parse_file('tests/test_files/single_contact_one_bad_field.txt')
        assert isinstance(result, Error)

        # single contact, one good field
        # single contact, one good field, whitespace before and after
        # single contact, multiple bad fields
        # single contact, multiple good fields
        # multiple contacts
        # multiple contacts, whitespace between
        # TEST LINEWRAPPING
        # No version
        # Wrong version

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

