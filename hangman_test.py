import unittest
from hangman import get_all_index


class HangmanTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def text_get_all_indexes_should_return_empty_if_there_is_no_match(self):
        # Given
        text = 'a'
        word = 'a'
        expected = []
        # When
        actual = get_all_index(text, word)
        # Then
        self.assertEqual(expected, actual)
    def text_get_all_indexes_should_return_2_or_3(self):
        # Given
        text = 'l'
        word = 'hello'
        expected = []
        # When
        actual = get_all_index(text, word)
        # Then
        self.assertEqual(expected, actual)

if __name__ == "__main__":

