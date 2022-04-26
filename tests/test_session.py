import unittest
from unittest.mock import patch

from qzlt.cards import Card
from qzlt.sets import Set
from qzlt.sessions import Session


class TestSession(unittest.TestCase):
    def test_init_session(self):
        test_set = Set(
            "French",
            "Common French expressions",
            [
                Card("Bonjour", "Hello"),
                Card("Je m'appelle Sam", "My name is Sam"),
                Card("Au revoir", "Bye"),
            ],
        )
        self.test_session = Session(test_set)

        self.assertIsNotNone(self.test_session)

    @patch("random.shuffle")
    def test_init_shuffle_session(self, mock_shuffle):
        test_set = Set(
            "French",
            "Common French expressions",
            [
                Card("Bonjour", "Hello"),
                Card("Je m'appelle Sam", "My name is Sam"),
                Card("Au revoir", "Bye"),
            ],
        )
        self.test_session = Session(test_set, shuffle=True)
        self.assertEqual(mock_shuffle.call_count, 1)


if __name__ == "__main__":
    unittest.main()
