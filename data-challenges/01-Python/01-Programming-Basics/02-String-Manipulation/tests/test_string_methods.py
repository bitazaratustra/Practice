# pylint: disable-all

import unittest

from string_methods import add_comma
from string_methods import belongs_to
from string_methods import count_repetition
from string_methods import is_a_question
from string_methods import replace
from string_methods import remove_surrounding_whitespaces
from string_methods import full_description_concatenation
from string_methods import full_description_formatting


class TestAddComma(unittest.TestCase):
    def test_strings_boris_romain_seb(self):
        """This method should return "boris, romain, seb" """
        self.assertEqual(add_comma("boris romain seb"), "boris, romain, seb")

    def test_strings_boris_seb_romain(self):
        """This method should return "boris, seb, romain" """
        self.assertEqual(add_comma("boris seb romain"), "boris, seb, romain")


class TestBelongsTo(unittest.TestCase):
    def test_include_word(self):
        """This method should return True as 'hey jude' contains 'jude'"""
        self.assertEqual(belongs_to("hey jude", "jude"), True)

    def test_do_not_include_word(self):
        """This method should return False as 'hey jude' doesn't contain 'joe'"""
        self.assertEqual(belongs_to("hey jude", "joe"), False)


class TestCountRep(unittest.TestCase):
    def test_numbers_0_0_1_2_0_on_0(self):
        """This method should return 3"""
        self.assertEqual(count_repetition("00120", "0"), 3)

    def test_numbers_0_0_1_2_0_on_3(self):
        """This method should return 0 if a_substring doesn't occur in a_string"""
        self.assertEqual(count_repetition("00120", "3"), 0)


class TestIsQuestion(unittest.TestCase):
    def test_is_a_question(self):
        """This method should return True when a_string ends with a '?'"""
        self.assertEqual(is_a_question("How are you?"), True)

    def test_is_not_a_question(self):
        """This method should return False when a_string doesn't end with a '?'"""
        self.assertEqual(is_a_question("Fine."), False)


class TestWhitespace(unittest.TestCase):
    def test_leading_whitespaces(self):
        """This method should work with leading whitespaces"""
        self.assertEqual(remove_surrounding_whitespaces("  hey yo"), "hey yo")

    def test_trailing_whitespaces(self):
        """This method should work with trailing whitespaces"""
        self.assertEqual(remove_surrounding_whitespaces("hey yo  "), "hey yo")

    def test_whitespaces(self):
        """This method should work with leading and trailing whitespaces"""
        self.assertEqual(remove_surrounding_whitespaces(" hey yo  "), "hey yo")


class TestReplace(unittest.TestCase):
    def test_casanova_to_cosonovo(self):
        """This method should correctly replace the letter(s) in the string"""
        self.assertEqual(replace("casanova", "a", "o"), "cosonovo")

    def test_kosovo_to_kasava(self):
        """This method should correctly replace the letter(s) in the string"""
        self.assertEqual(replace("kosovo", "o", "a"), "kasava")


class TestConcat(unittest.TestCase):
    def test_john_doe_33_concatenation(self):
        """This method should correctly return the full name and the age"""
        self.assertEqual(full_description_concatenation("John", "Doe", 33), "John Doe is 33")


class TestFString(unittest.TestCase):
    def test_john_doe_33_formatting(self):
        """This method should correctly return the full name and the age"""
        self.assertEqual(full_description_formatting("John", "Doe", 33), "John Doe is 33")
