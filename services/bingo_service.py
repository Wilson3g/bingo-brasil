import random
from typing import List

from repository.bingo_repository_in_memory import (
    BingoRepositoryInterface,
    BingoInMemoryReposository
)

class BingoService:
    def __init__(self, respository: BingoRepositoryInterface | BingoInMemoryReposository):
        self.__repository = respository if respository else BingoRepositoryInterface()

    def get_bingo(self):
        return {"Hello": "World"}
    
    def __get_numbers(self, start: int, end: int) -> List[int]:
        numbers_list: list[int] = []
        while True:
            number = random.randint(start, end)
            if number not in numbers_list: numbers_list.append(number)
            if len(numbers_list) == 5: break
        return sorted(numbers_list)

    def get_card(self) -> List[list]:
        cards = [
            self.__get_numbers(1, 15),
            self.__get_numbers(16, 30),
            self.__get_numbers(31, 45),
            self.__get_numbers(46, 60),
            self.__get_numbers(61, 75)
        ]
        card_ordered_list: list[int] = sum(cards, [])
        all_cards: list[int] = self.__repository.get_all_cards()
        for card in all_cards:
            if card == card_ordered_list:
                return self.get_card()
        self.__repository.insert_card(card_ordered_list)

        return cards
    
    def get_drawn_numbers(self, start: int = 1, end: int = 75) -> int:
        drawn_numbers: list[int] = self.__repository.get_drawn_numbers()
        if len(drawn_numbers) >= end:
            return 0
        number: int = random.randint(start, end)
        if number in drawn_numbers:
            return self.get_drawn_numbers(start, end)
        self.__repository.insert_drawn_number(number)
        return number
    
    def get_drawn_numbers_list_and_percentage(self, total_bingo_numbers: int = 75) -> tuple:
        drawn_numbers: list[int] = self.__repository.get_drawn_numbers()
        percentage: float = (len(drawn_numbers)/total_bingo_numbers) * 100
        return drawn_numbers, round(percentage, 2)

    def has_bingo(self) -> bool:
        bingo: bool = False
        bingo_numbers: list[int] = self.__repository.get_drawn_numbers()
        cards = self.__repository.get_all_cards()
        for card in cards:
            if set(card).issubset(set(bingo_numbers)):
                return True
        return bingo