import unittest

from controllers.bingo_controller import Bingo


class TestBingo(unittest.TestCase):
    def setUp(self):
        self.bingo = Bingo()

    def test_bingo_card_total_columns(self):
        """Verifica se a quantidade de colunas retornadas é igual a 5"""
        card = self.bingo.get_card()
        self.assertEqual(len(card), 5)

    def test_if_cards_numbers_is_sorted(self):
        """Verifica se os números em cada coluna estão ordnedos de forma ascendente"""
        card = self.bingo.get_card()
        card_sorted = [
            sorted(card[0]),
            sorted(card[1]),
            sorted(card[2]),
            sorted(card[3]),
            sorted(card[4])
        ]
        self.assertListEqual(card, card_sorted)

    def test_if_card_has_unique_numbers(self):
        """Verificar se os números nas colunas se repetem"""
        card = self.bingo.get_card()
        card_column_b = len( set( [ item for item in card[0] if card.count( item ) > 1] ) )
        card_column_i = len( set( [ item for item in card[1] if card.count( item ) > 1] ) )
        card_column_n = len( set( [ item for item in card[2] if card.count( item ) > 1] ) )
        card_column_g = len( set( [ item for item in card[3] if card.count( item ) > 1] ) )
        card_column_o = len( set( [ item for item in card[4] if card.count( item ) > 1] ) )
        self.assertEqual(card_column_b, 0)
        self.assertEqual(card_column_i, 0)
        self.assertEqual(card_column_n, 0)
        self.assertEqual(card_column_g, 0)
        self.assertEqual(card_column_o, 0)

    def test_if_drawn_number_is_between_one_and_three(self):
        drawn_number = self.bingo.get_drawn_numbers(1, 3)
        self.assertTrue(drawn_number, drawn_number >= 1 and drawn_number <= 3)

    def test_if_drawn_number_is_unique(self):
        drawn_numbers_list = []
        for _ in range(0,3):
            drawn_numbers_list.append(self.bingo.get_drawn_numbers(1, 3))
        number_of_non_unique_numbers = len( set( [ item for item in drawn_numbers_list if drawn_numbers_list.count( item ) > 1] ) )
        self.assertEqual(number_of_non_unique_numbers, 0)

    def test_if_drawn_number_return_zero(self):
        for _ in range(0,3):
            drawn_number = self.bingo.get_drawn_numbers(1,2)
        self.assertEqual(drawn_number, 0)

    def test_get_drawn_numbers_list_is_empty(self):
        drawn_numbers, _ = self.bingo.get_drawn_numbers_list_and_percentage()
        self.assertEqual(type(drawn_numbers), list)
        self.assertEqual(len(drawn_numbers), 0)

    def test_get_drawn_numbers_list(self):
        for _ in range(0,2):
            self.bingo.get_drawn_numbers(1,2)
        drawn_numbers, _ = self.bingo.get_drawn_numbers_list_and_percentage()
        self.assertEqual(type(drawn_numbers), list)
        self.assertEqual(len(drawn_numbers), 2)

    def test_percentage_of_drawn_numbers_list(self):
        _, percentage = self.bingo.get_drawn_numbers_list_and_percentage(total_bingo_numbers=2)
        self.assertEqual(percentage, 0.0)
        self.bingo.get_drawn_numbers(1,2)
        _, percentage = self.bingo.get_drawn_numbers_list_and_percentage(total_bingo_numbers=2)
        self.assertEqual(percentage, 50.0)
        self.bingo.get_drawn_numbers(1,2)
        _, percentage = self.bingo.get_drawn_numbers_list_and_percentage(total_bingo_numbers=2)
        self.assertEqual(percentage, 100.0)


if __name__ == '__main__':
    unittest.main()