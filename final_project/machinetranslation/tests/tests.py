import unittest
from translator import english_to_french, french_to_english


class TestTranslatorToEnglish(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_french_to_english_none(self):
        self.assertIsNone(french_to_english(""))

class TestTranslatorToFrench(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_english_to_french_none(self):
        self.assertIsNone(english_to_french(""))
