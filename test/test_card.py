import unittest

from qzlt.cards import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.test_card = Card("Bonjour", "Hello")

    def test_init_card(self):
        self.assertIsNotNone(self.test_card)
        self.assertEqual(self.test_card._term, "Bonjour")
        self.assertEqual(self.test_card._definition, "Hello")

    def test_get_term(self):
        self.assertEqual(self.test_card._term, "Bonjour")

    def test_set_term(self):
        self.test_card._term = "Au revoir"
        self.assertEqual(self.test_card._term, "Au revoir")

    def test_get_definition(self):
        self.assertEqual(self.test_card._definition, "Hello")

    def test_set_definition(self):
        self.test_card._definition = "Goodbye"
        self.assertEqual(self.test_card._definition, "Goodbye")


if __name__ == "__main__":
    unittest.main()
