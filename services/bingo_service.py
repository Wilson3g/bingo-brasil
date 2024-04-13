import random
from typing import List

from repository.bingo_repository_in_memory import (
    BingoRepositoryInterface
)

class BingoService:
    def __init__(self, respository):
        self.__repository = respository if respository else BingoRepositoryInterface()

    def get_bingo(self):
        return {"Hello": "World"}
    
    def __get_numbers(self, start: int, end: int) -> List[int]:
        numbers_list = []
        while True:
            number = random.randint(start, end)
            if number not in numbers_list: numbers_list.append(number)
            if len(numbers_list) == 5: break
        return sorted(numbers_list)

    def get_card(self) -> List[list]:
        card = [
            self.__get_numbers(1, 15),
            self.__get_numbers(16, 30),
            self.__get_numbers(31, 45),
            self.__get_numbers(46, 60),
            self.__get_numbers(61, 75)
        ]
        card_ordered_list = sum(card, [])
        for card_database in self.__repository.get_all_cards():
            if card_database == card_ordered_list:
                return self.get_card()
        self.__repository.insert_card(card_ordered_list)

        return card
    
    def get_drawn_numbers(self, start: int = 1, end: int = 75) -> int:
        if len(self.__repository.get_drawn_numbers()) >= end:
            return 0
        number = random.randint(start, end)
        if number in self.__repository.get_drawn_numbers():
            return self.get_drawn_numbers(start, end)
        self.__repository.insert_drawn_number(number)
        return number
    
    def get_drawn_numbers_list_and_percentage(self, total_bingo_numbers: int = 75) -> tuple:
        percentage = (len(self.__repository.get_drawn_numbers())/total_bingo_numbers) * 100
        return self.__repository.get_drawn_numbers(), round(percentage, 2)

    def has_bingo(self) -> bool:
        bingo = False
        bingo_numbers = self.__repository.get_drawn_numbers()
        for card in self.__repository.get_all_cards():
            if set(card).issubset(set(bingo_numbers)):
                return True
        return bingo