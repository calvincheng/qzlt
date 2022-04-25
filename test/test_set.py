import unittest

from qzlt.sets import Set
from qzlt.cards import Card


class TestSet(unittest.TestCase):
    def setUp(self):
        self.test_set = Set("French", "Common French expressions")

    def test_init_set(self):
        self.assertIsNotNone(self.test_set)
        self.assertEqual(self.test_set._title, "French")
        self.assertEqual(self.test_set._description, "Common French expressions")
        self.assertEqual(len(self.test_set), 0)

    def test_len_set(self):
        self.test_set.add(Card("Bonjour", "Hello"))
        self.test_set.add(Card("Je m'appelle Sam", "My name is Sam"))
        self.test_set.add(Card("Au revoir", "Bye"))
        self.assertEqual(len(self.test_set), 3)

    def test_add_card(self):
        self.test_set.add(Card("Bonjour", "Hello"))
        self.assertIsInstance(self.test_set._cards[0], Card)
        self.assertEqual(len(self.test_set), 1)

    def test_delete_card(self):
        self.test_set.add(Card("Bonjour", "Hello"))
        self.test_set.add(Card("Je m'appelle Sam", "My name is Sam"))
        self.test_set.add(Card("Au revoir", "Bye"))
        self.assertEqual(len(self.test_set), 3)

        self.test_set.delete(2)  # Delete 'Au revoir' card
        self.assertEqual(len(self.test_set), 2)
        self.assertEqual(self.test_set._cards[0]._term, "Bonjour")
        self.assertEqual(self.test_set._cards[1]._term, "Je m'appelle Sam")

    def test_get_title(self):
        self.assertEqual(self.test_set._title, "French")

    def test_set_title(self):
        self.test_set._title = "Spanish"
        self.assertEqual(self.test_set._title, "Spanish")

    def test_get_description(self):
        self.assertEqual(self.test_set._description, "Common French expressions")

    def test_set_description(self):
        self.test_set._description = "Expresiones comunes en español"
        self.assertEqual(self.test_set._description, "Expresiones comunes en español")

    def test_get_cards(self):
        self.assertListEqual(self.test_set._cards, [])

    def test_set_cards(self):
        new_cards = [
            Card("Bonjour", "Hello"),
            Card("Je m'appelle Sam", "My name is Sam"),
            Card("Au revoir", "Bye"),
        ]
        self.test_set._cards = new_cards
        self.assertListEqual(self.test_set._cards, new_cards)


if __name__ == "__main__":
    unittest.main()
